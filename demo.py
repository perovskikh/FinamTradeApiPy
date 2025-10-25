#!/usr/bin/env python3
"""
Demo script for FinamTradeApiPy library
This script demonstrates the library structure and available methods without requiring actual API credentials.
"""

import asyncio
import os
from pprint import pprint

from finam_trade_api import Client, TokenManager


def display_library_info():
    """Display information about the library and its capabilities."""
    print("=" * 80)
    print("FinamTradeApiPy - Async REST Client for Finam Trade API")
    print("=" * 80)
    print("\nThis is a Python library for interacting with Finam Trade API.")
    print("\nLibrary Version: 4.1.0")
    print("\nKey Features:")
    print("  • Asynchronous REST client using aiohttp")
    print("  • Type-safe models using Pydantic")
    print("  • Support for:")
    print("    - Access token management")
    print("    - Account information and transactions")
    print("    - Assets and instruments data")
    print("    - Market data (quotes, trades, order books)")
    print("    - Order management")
    print("\n" + "=" * 80)


def display_client_structure():
    """Display the client structure and available methods."""
    print("\nClient Structure:")
    print("-" * 80)
    print("\nThe main Client class provides access to the following modules:")
    print("\n1. access_tokens - Token management")
    print("   • set_jwt_token()")
    print("   • get_jwt_token_details()")
    print("\n2. account - Account operations")
    print("   • get_account_info(account_id)")
    print("   • get_transactions(request)")
    print("   • get_trades(request)")
    print("\n3. assets - Asset information")
    print("   • get_exchanges()")
    print("   • get_options_chain(underlying_symbol)")
    print("   • get_schedule(instrument_symbol)")
    print("   • get_asset(instrument_symbol, account_id)")
    print("   • get_asset_params(instrument_symbol, account_id)")
    print("\n4. instruments - Market data")
    print("   • get_bars(request)")
    print("   • get_last_quote(symbol)")
    print("   • get_last_trades(symbol)")
    print("   • get_order_book(symbol)")
    print("\n5. orders - Order management")
    print("   • place_order(request)")
    print("   • get_order(order_id)")
    print("   • cancel_order(order_id)")
    print("-" * 80)


async def demo_client_initialization():
    """Demonstrate client initialization (without actual API call)."""
    print("\nClient Initialization Example:")
    print("-" * 80)
    print("\n# Initialize client with token manager")
    print("token = os.getenv('TOKEN')  # Get token from environment")
    print("client = Client(TokenManager(token))")
    print("\n# Set JWT token for API access")
    print("await client.access_tokens.set_jwt_token()")
    print("\n# Now you can use the client to access various API endpoints")
    print("\nNOTE: To actually use this library, you need:")
    print("  1. A valid API token from https://tradeapi.finam.ru/docs/tokens")
    print("  2. Set it as TOKEN environment variable")
    print("  3. (Optional) Set ACCOUNT_ID for account-specific operations")
    print("-" * 80)


def display_examples():
    """Display information about available examples."""
    print("\nAvailable Examples:")
    print("-" * 80)
    print("\nThe 'examples/' directory contains working code samples:")
    print("\n• access_token.py  - Token authentication")
    print("• account.py       - Account information and transactions")
    print("• assets.py        - Asset and exchange information")
    print("• instruments.py   - Market data (bars, quotes, order book)")
    print("\nTo run an example:")
    print("  1. Set your TOKEN environment variable")
    print("  2. Set ACCOUNT_ID if needed")
    print("  3. Run: python examples/<example_name>.py")
    print("-" * 80)


def display_installation():
    """Display installation instructions."""
    print("\nInstallation:")
    print("-" * 80)
    print("\nFrom PyPI:")
    print("  pip install finam-trade-api")
    print("\nOr with Poetry:")
    print("  poetry add finam-trade-api")
    print("\nDevelopment installation:")
    print("  poetry install")
    print("-" * 80)


async def main():
    """Main demo function."""
    display_library_info()
    display_client_structure()
    await demo_client_initialization()
    display_examples()
    display_installation()
    
    print("\n" + "=" * 80)
    print("For more information, visit:")
    print("  • Documentation: https://tradeapi.finam.ru/docs/about/")
    print("  • GitHub: https://github.com/DBoyara/FinamTradeApiPy")
    print("  • PyPI: https://pypi.org/project/finam-trade-api/")
    print("=" * 80 + "\n")
    
    token = os.getenv("TOKEN")
    if token:
        print("\n✓ TOKEN environment variable is set!")
        print("  You can run the examples in the 'examples/' directory.")
    else:
        print("\n✗ TOKEN environment variable is not set.")
        print("  To use the API, get a token from https://tradeapi.finam.ru/docs/tokens")
        print("  and set it as an environment variable.")


if __name__ == "__main__":
    asyncio.run(main())
