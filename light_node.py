import time
import socket

PEERS = [
    ("node1.lazvchain.org", 9333),
    ("node2.lazvchain.org", 9333),
]

print("LAZV Light Node running (no wallet, no keys)")

while True:
    for host, port in PEERS:
        try:
            s = socket.create_connection((host, port), timeout=5)
            s.send(b"ping")
            s.close()
            print(f"Connected to {host}")
        except:
            print(f"Peer {host} offline")
    time.sleep(30)