from flask import Flask, jsonify, request
import time, hashlib

app = Flask(__name__)
chain = []

def block(prev):
    return {
        "index": len(chain),
        "time": time.time(),
        "prev": prev,
        "hash": hashlib.sha256(str(prev).encode()).hexdigest()
    }

chain.append(block("GENESIS"))

@app.route("/chain")
def get_chain():
    return jsonify(chain)

@app.route("/mine")
def mine():
    b = block(chain[-1]["hash"])
    chain.append(b)
    return jsonify(b)

@app.route("/ping", methods=["POST"])
def ping():
    return {"ok": True}

app.run(host="0.0.0.0", port=8000)