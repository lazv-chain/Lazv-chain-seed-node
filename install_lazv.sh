#!/bin/bash
echo "[INSTALL] Installing LAZV Chain..."
pkg install -y python git || apt install -y python3 git
pip install --upgrade pip
pip install flask requests qrcode

echo "[INSTALL] Cloning LAZV-CHAIN..."
git clone https://github.com/yourrepo/LAZV-CHAIN.git
cd LAZV-CHAIN

echo "[INSTALL] Running node..."
python node_global.py