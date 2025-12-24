# relayer.py — Builder-Ready Proof Signing
import json, requests, time

# CONFIG
NODE_URL = "http://localhost:8000"  # node.py endpoint
RELAYER_ID = "relayer_A"
MULTISIG_THRESHOLD = 2  # contoh 2-of-3

# Dummy local private key (replace dengan multisig signing)
PRIVATE_KEY = "dummy_private_key"

# fetch Polygon events (simulasi)
def fetch_locked_events():
    # Contoh: ambil dari API Polygon bridge atau JSON dummy
    return [
        {"user": "0xUser1", "amount": 100, "nonce": 1},
        {"user": "0xUser2", "amount": 50, "nonce": 2}
    ]

# sign proof skeleton
def sign_proof(event):
    # Dummy sign
    event["signature"] = f"signed_by_{RELAYER_ID}"
    return event

# submit proof ke node
def submit_proof(proof):
    try:
        r = requests.post(f"{NODE_URL}/mint", json=proof)
        print("Submitted:", proof, "Response:", r.text)
    except Exception as e:
        print("Error submitting proof:", e)

# main loop
if __name__ == "__main__":
    while True:
        events = fetch_locked_events()
        for ev in events:
            proof = sign_proof(ev)
            submit_proof(proof)
        time.sleep(10)  # cek tiap 10 detik
