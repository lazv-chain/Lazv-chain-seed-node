# LAZV Chain Explorer Guide

This guide explains how to deploy the LAZV Chain Explorer (read-only, live stats).

## Features
- Live stats from node.py:
  - Total blocks
  - Minted WLUZV
  - Burned WLUZV
  - Online peers
- Auto-refresh every 5 seconds
- Minimal & builder-friendly

## Deployment
1. Make sure node.py is running and accessible.
2. Upload `explorer.html` to:
   - Vercel
   - Cloudflare Pages
   - VPS / web server
3. Adjust `NODE_URL` in explorer.html to point to your node `/stats` endpoint.
4. Open explorer.html in browser.

## Optional Enhancements
- Add charts for minted/burned WLUZV
- Add peer status dashboard
- Add block list with timestamp and hash
