#!/bin/bash

while true; do
  if ip route | grep -q wlan0; then
    echo "📶 Wi‑Fi detected → LAZV node ON"
    python light_node.py &
    NODE_PID=$!
    wait $NODE_PID
  else
    echo "📵 No Wi‑Fi → LAZV node OFF"
    pkill -f light_node.py
  fi
  sleep 60
done