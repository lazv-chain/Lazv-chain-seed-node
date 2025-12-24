# LAZV Chain Bridge Guide

## 1. Polygon → LAZV
- User lock LUZV (ERC-20)
- Event Locked tercatat di chain
- Relayer sign proof (threshold multisig)
- node.py mint WLUZV (1:1 backed)

## 2. LAZV → Polygon
- User burn WLUZV
- Submit proof JSON ke relayer
- Bridge unlock LUZV ke user

## 3. Security
- Multisig owner recommended
- Event-only verification
- No admin mint
- Trust-minimized
