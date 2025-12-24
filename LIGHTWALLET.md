# LAZV Chain Light Wallet

A minimal wallet for LAZV Chain users.

## Features
- View balance (WLUZV / LAZV)
- Mint WLUZV from Polygon via bridge (requires proof relayer)
- Burn WLUZV to unlock LUZV on Polygon
- Connect to multiple node endpoints

## How to Use
1. Open wallet HTML/JS in browser
2. Connect to preferred LAZV node
3. Use `mint` / `burn` buttons to interact with node
4. View transaction history (read-only from node / explorer)

## Security Notes
- Wallet is light, no private key custody
- Proof signing handled by relayer node
- Keep node URL trusted
