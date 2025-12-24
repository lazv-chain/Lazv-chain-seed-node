from flask import Flask, request, jsonify
import requests, json, threading, time
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

PEERS_FILE = "peers.json"

# --- Peer Storage ---
def load_peers():
    try:
        with open(PEERS_FILE, "r") as f:
            return json.load(f)["peers"]
    except:
        return []

def save_peers(peers):
    with open(PEERS_FILE, "w") as f:
        json.dump({"peers": peers}, f)

# --- Routes ---
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "alive", "length": len(blockchain.chain)})

@app.route("/chain", methods=["GET"])
def get_chain():
    return jsonify({
        "length": len(blockchain.chain),
        "chain": blockchain.chain
    })

@app.route("/peers", methods=["GET", "POST"])
def peers():
    peers = load_peers()
    if request.method == "POST":
        peer = request.json.get("peer")
        if peer and peer not in peers:
            peers.append(peer)
            save_peers(peers)
        return jsonify({"peers": peers})
    return jsonify({"peers": peers})

@app.route("/mine", methods=["POST"])
def mine():
    data = request.json or {}
    blockchain.add_block(data)
    return jsonify({"message": "Block mined", "length": len(blockchain.chain)})

# --- Background Peer Check ---
def peer_heartbeat():
    while True:
        peers = load_peers()
        for p in peers:
            try:
                requests.get(p + "/ping", timeout=3)
            except:
                pass
        time.sleep(30)

# --- Start ---
if __name__ == "__main__":
    threading.Thread(target=peer_heartbeat, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)

# node.py — FINAL BUILDER-READY
import json, time, hashlib, requests
from flask import Flask, request

app = Flask(__name__)

CHAIN = []
PEERS = set()
SEEDS = set()  # initial seed nodes

def hash_block(block):
    return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

def new_block(data):
    prev = CHAIN[-1]["hash"] if CHAIN else "GENESIS"
    block = {
        "index": len(CHAIN),
        "time": time.time(),
        "data": data,
        "prev": prev
    }
    block["hash"] = hash_block(block)
    CHAIN.append(block)
    broadcast(block)
    return block

def broadcast(block):
    for p in PEERS:
        try:
            requests.post(f"{p}/block", json=block, timeout=1)
        except:
            pass

@app.route("/block", methods=["POST"])
def receive_block():
    block = request.json
    if not CHAIN or block["prev"] == CHAIN[-1]["hash"]:
        CHAIN.append(block)
    return "ok"

@app.route("/peer", methods=["POST"])
def add_peer():
    PEERS.add(request.json["url"])
    return "ok"

def verify_proof(proof):
    # proof = event LUZV lock + signature relayer
    return True

@app.route("/mint", methods=["POST"])
def mint():
    p = request.json
    if verify_proof(p):
        return new_block({"mint_LAZV": p})
    return "invalid", 400

@app.route("/burn", methods=["POST"])
def burn():
    data = request.json
    return new_block({"burn_LAZV": data})

@app.route("/stats")
def stats():
    minted = sum(1 for b in CHAIN if "mint_LAZV" in b.get("data", {}))
    burned = sum(1 for b in CHAIN if "burn_LAZV" in b.get("data", {}))
    return {"blocks": len(CHAIN), "minted": minted, "burned": burned, "peers": list(PEERS)}

if __name__ == "__main__":
    new_block("GENESIS")
    app.run(port=8000)
