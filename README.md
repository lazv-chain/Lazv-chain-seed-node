# LAZV Chain

LAZV Chain = Sovereign blockchain anchored to Polygon (LUZV ERC-20).

## Assets
- LUZV (Polygon) → Digital Silver / Platinum Anchor
- LAZV (LAZV Chain) → eMass / Gold, native coin, 1:1 backed
- WLUZV (LAZV Chain) → optional wrapped coin

## Node
- node.py → Python node, peer discovery, mint/burn WLUZV
- Run: `python node.py`
- Connect to peers via `/peer`

## Bridge
- Polygon bridge event → LAZV mint / burn
- Multisig owner recommended
- Proof-only verification

## Philosophy
- Polygon = Mother Chain
- LAZV = Sovereign Execution Layer
- Community-run, trust-minimized, builder-grade

# LAZV Chain

LAZV is a minimal, community-run public blockchain.

There is no owner.
There is no central server.
Anyone can run a node.

This chain is designed to survive even if the original seed nodes go offline.

---

## Philosophy

LAZV follows early Bitcoin principles:

- Open source
- Permissionless
- Community-operated
- No VC
- No founder control

If this repository exists, the chain can exist.

---

## Requirements

- Python 3.8+
- Internet connection
- Any device:
  - Android (Termux)
  - Laptop / PC
  - VPS (optional)

---

## How to Run a Node

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/LAZV-chain.git
cd LAZV-chain
2. Install dependencies
Salin kode
Bash
pip install flask requests
3. Run the node
Salin kode
Bash
python node.py
Your node will:
Start a local blockchain
Connect to known peers (if available)
Accept incoming peers
Temporary Seed Nodes (Bootstrap Only)
These seeds are temporary and may go offline at any time.
Salin kode

- https://your-replit-url.repl.co
- http://your-vps-ip:5000
⚠️ Important: This blockchain does NOT depend on these seeds. You are expected to run your own node.
Peer Discovery
Peers are stored locally in peers.json.
If all seeds go offline:
Nodes that already know each other will continue
New nodes can manually add peers
This is intentional.
Data Persistence
Blockchain data is stored locally. No cloud dependency. No central database.
Governance
There is no on-chain governance. There is no admin key.
Consensus emerges from node operators.
Disclaimer
This is experimental software. Use at your own risk. No financial guarantees.
Join the Network
Run a node. Share your IP with others. Let the chain live.
Salin kode

---

## 📄 MANIFESTO.md (BUILDER-STYLE, KUAT)

```md
# LAZV Manifesto

LAZV exists because blockchains should not depend on people.

No founder permanence.
No infrastructure dependency.
No subscription-based decentralization.

If a blockchain dies when its creator leaves,
it was never decentralized.

LAZV is designed to survive abandonment.

Run it.
Fork it.
Forget it.

If others still run it, it lives.

That is the point.
📄 LICENSE (MIT – WAJIB)
Salin kode
Md
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
👉 (pakai MIT standard, jangan diubah)
📄 peers.json (AWAL)
Salin kode
Json
{
  "peers": []
}

LAZV-CHAIN/
├─ node.py
├─ relayer.py
├─ explorer.html
├─ seeds.json
├─ peers.json
├─ README.md
├─ BRIDGE.md
├─ EXPLORER.md
├─ LIGHTWALLET.md
├─ MANIFESTO.md
└─ LICENSE (MIT)
