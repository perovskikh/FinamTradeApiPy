# FinamTradeApiPy - Replit Project

## Overview
This is a Python library (FinamTradeApiPy) for interacting with the Finam Trade API. It provides an asynchronous REST client with type-safe models for trading operations, market data, and account management.

**Project Type**: Python Library (not a web application)
**Version**: 4.1.0
**Main Technologies**: 
- Python 3.11+
- aiohttp (async HTTP client)
- pydantic (data validation)
- Poetry (dependency management)

## Current State
- ✅ All dependencies installed via Poetry
- ✅ Demo script created (demo.py) to showcase library capabilities
- ✅ Workflow configured to run the demo
- ✅ Project ready for development and testing

## Project Structure
```
finam_trade_api/        # Main library package
├── access/             # Token management
├── account/            # Account operations
├── assets/             # Asset information
├── base_client/        # Base client and token manager
├── instruments/        # Market data
└── order/              # Order management

examples/               # Usage examples
├── access_token.py     # Token authentication example
├── account.py          # Account operations example
├── assets.py           # Assets example
└── instruments.py      # Market data example

tests/                  # Test suite
demo.py                 # Interactive demo script
```

## How to Use This Library

### 1. Get API Credentials
- Register and generate a token at: https://tradeapi.finam.ru/docs/tokens
- Set the token as an environment variable: `TOKEN`
- (Optional) Set `ACCOUNT_ID` for account-specific operations

### 2. Run Examples
The `examples/` directory contains working code samples:
- `python examples/access_token.py` - Token authentication
- `python examples/account.py` - Account information
- `python examples/assets.py` - Asset data
- `python examples/instruments.py` - Market data

### 3. Use in Your Code
```python
import os
from finam_trade_api import Client, TokenManager

async def main():
    token = os.getenv("TOKEN")
    client = Client(TokenManager(token))
    await client.access_tokens.set_jwt_token()
    
    # Use the client...
    account_info = await client.account.get_account_info(account_id)
```

## Library Capabilities

### Access Token Management
- `client.access_tokens.set_jwt_token()` - Authenticate with JWT
- `client.access_tokens.get_jwt_token_details()` - Get token details

### Account Operations
- `client.account.get_account_info(account_id)` - Get account information
- `client.account.get_transactions(request)` - Get transaction history
- `client.account.get_trades(request)` - Get trade history

### Asset Information
- `client.assets.get_exchanges()` - Get available exchanges
- `client.assets.get_options_chain(symbol)` - Get options chain
- `client.assets.get_schedule(symbol)` - Get trading schedule
- `client.assets.get_asset(symbol, account_id)` - Get asset details

### Market Data
- `client.instruments.get_bars(request)` - Get historical bars
- `client.instruments.get_last_quote(symbol)` - Get last quote
- `client.instruments.get_last_trades(symbol)` - Get recent trades
- `client.instruments.get_order_book(symbol)` - Get order book

### Order Management
- `client.orders.place_order(request)` - Place an order
- `client.orders.get_order(order_id)` - Get order details
- `client.orders.cancel_order(order_id)` - Cancel an order

## Development

### Running Tests
```bash
poetry run pytest
```

### Code Quality
The project uses:
- `ruff` for linting and formatting
- `mypy` for type checking
- `bandit` for security analysis
- `pre-commit` for automated checks

### Running Pre-commit Hooks
```bash
poetry run pre-commit run --all-files
```

## Recent Changes
- **2025-10-25**: Initial Replit setup
  - Installed all dependencies via Poetry
  - Created demo.py for showcasing library capabilities
  - Configured workflow for running the demo
  - Created replit.md for project documentation

## User Preferences
No specific user preferences recorded yet.

## Notes
- This is a library project, not a standalone application
- Requires valid Finam Trade API credentials to use
- All API interactions are asynchronous (uses asyncio)
- The demo script can run without credentials and shows library structure
