# LNbits on Replit

## Overview
LNbits is a free and open-source Lightning Network wallet and accounts system. This is the official LNbits repository configured to run on Replit.

**Project Type:** Bitcoin/Lightning Network Payment Platform
**Tech Stack:** 
- Backend: Python (FastAPI, Uvicorn)
- Frontend: Vue.js 3, Quasar Framework
- Database: SQLite (default) / PostgreSQL (optional)
- Package Manager: UV (Python), npm (Node.js)

## Current State
✅ **Successfully configured and running on Replit**
- Server running on port 5000 (0.0.0.0)
- Using FakeWallet funding source for development/demo
- Admin UI enabled
- SQLite database in `./data` folder
- First-time setup page accessible

## Project Structure
```
lnbits/
├── core/           # Core application logic
├── wallets/        # Lightning wallet integrations
├── static/         # Frontend assets (Vue.js, bundled)
├── extensions/     # Extension system (installed separately)
├── __main__.py     # Application entry point
├── app.py          # FastAPI app creation
├── server.py       # Uvicorn server launcher
└── settings.py     # Configuration management

docs/               # Documentation
tests/              # Test suite
tools/              # Utility scripts
run_lnbits.sh       # Startup script for Replit
```

## Running the Application

### Development
The application runs automatically via the configured workflow:
- Workflow: "LNbits Server"
- Command: `bash run_lnbits.sh`
- Port: 5000
- Host: 0.0.0.0

### Manual Start
```bash
bash run_lnbits.sh
```

Or with uv directly:
```bash
uv run lnbits --host 0.0.0.0 --port 5000
```

## Configuration

### Environment Variables (set in run_lnbits.sh)
- `HOST=0.0.0.0` - Server host (required for Replit)
- `PORT=5000` - Server port
- `LNBITS_BACKEND_WALLET_CLASS=FakeWallet` - Demo wallet (no real Bitcoin)
- `LNBITS_DATA_FOLDER=./data` - Database location
- `FORWARDED_ALLOW_IPS=*` - Allow proxy requests (required for Replit)
- `LNBITS_ADMIN_UI=true` - Enable admin interface

### Funding Sources
Currently using **FakeWallet** for demo purposes. To use real Lightning:
1. Edit `run_lnbits.sh`
2. Change `LNBITS_BACKEND_WALLET_CLASS` to a real wallet type:
   - `LndRestWallet`, `CoreLightningWallet`, `EclairWallet`, etc.
3. Add corresponding wallet credentials
4. See `.env.example` for all wallet configurations

## First-Time Setup
1. Access the application in the Replit webview
2. Create superuser account on the first install page
3. Alternatively, run: `uv run lnbits-cli superuser`

## Key Features
- **Multi-wallet system** - Create isolated wallets with separate API keys
- **Extension system** - Add features like Points of Sale, LNURLp, etc.
- **Admin dashboard** - Manage users, settings, funding sources
- **RESTful API** - Full API access for integrations
- **Node management** - Light node management UI

## Development Commands

### Package Management
```bash
# Install Python dependencies
uv sync

# Install Node.js dependencies
npm install

# Bundle frontend assets
npm run bundle
```

### Testing
```bash
# Run all tests
make test

# Run specific test suites
make test-unit
make test-api
make test-wallets
```

### Code Quality
```bash
# Format code
make format

# Type checking
make mypy
make pyright

# Linting
make check
```

## Deployment
The application is configured for deployment with:
- **Target:** VM (always-running)
- **Command:** `bash run_lnbits.sh`
- Suitable for: Wallets, payment processors, always-on services

## Important Notes

### Security
- **FakeWallet is for DEMO only** - No real Bitcoin transactions
- Change `AUTH_SECRET_KEY` for production
- Use strong passwords for superuser account
- Consider using PostgreSQL for production

### Data Persistence
- Data stored in `./data` folder (SQLite database)
- Includes wallets, transactions, users, settings
- Not committed to git (in .gitignore)

### Extensions
- Install extensions via Admin UI
- Default extension: tpos (Point of Sale)
- Extensions stored in `./lnbits/extensions/`
- Browse more: https://extensions.lnbits.com/

## Resources
- **Official Docs:** https://docs.lnbits.org
- **Website:** https://lnbits.com
- **Extensions:** https://extensions.lnbits.com/
- **GitHub:** https://github.com/lnbits/lnbits
- **Community:** https://t.me/lnbits

## Recent Changes
- 2025-11-13: Initial Replit configuration
  - Created run_lnbits.sh startup script
  - Configured workflow for port 5000
  - Set up deployment configuration
  - Verified frontend and backend working

## Troubleshooting

### Server won't start
- Check logs in the workflow panel
- Ensure port 5000 is not in use
- Verify all dependencies installed: `uv sync`

### Frontend not loading
- Frontend bundles are pre-built in `lnbits/static/`
- If missing, run: `npm run bundle`

### Database issues
- Delete `./data` folder to reset (WARNING: loses all data)
- Or run migrations: `uv run lnbits-cli db migrate`

## User Preferences
- None set yet
