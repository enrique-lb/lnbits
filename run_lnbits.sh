#!/bin/bash

# LNbits startup script for Replit

# Set required environment variables
export HOST=0.0.0.0
export PORT=5000
export LNBITS_BACKEND_WALLET_CLASS=FakeWallet
export LNBITS_DATA_FOLDER="./data"
export FORWARDED_ALLOW_IPS="*"
export LNBITS_ADMIN_UI=true
export FAKE_WALLET_SECRET="ToTheMoon1"
export LNBITS_DENOMINATION=sats
export DEBUG=false

# Run LNbits
uv run lnbits --host 0.0.0.0 --port 5000
