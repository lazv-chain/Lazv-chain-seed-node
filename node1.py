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
