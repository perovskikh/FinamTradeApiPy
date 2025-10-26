~/workspace$ ls
demo.py  examples  finam_trade_api  LICENSE  poetry.lock  pyproject.toml  README.md  replit.md  tests
~/workspace$ python3 examples/access_token.py
Traceback (most recent call last):
  File "/home/runner/workspace/examples/access_token.py", line 18, in <module>
    print(asyncio.run(main()))
          ^^^^^^^^^^^^^^^^^^^
  File "/nix/store/7d088dip86hlzri9sk0h78b63yfmx0a0-python3-3.11.13/lib/python3.11/asyncio/runners.py", line 190, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/nix/store/7d088dip86hlzri9sk0h78b63yfmx0a0-python3-3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/nix/store/7d088dip86hlzri9sk0h78b63yfmx0a0-python3-3.11.13/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/home/runner/workspace/examples/access_token.py", line 10, in main
    await client.access_tokens.set_jwt_token()
  File "/home/runner/workspace/finam_trade_api/access/access_token.py", line 47, in set_jwt_token
    raise FinamTradeApiError(f"code={err.code} | message={err.message} | details={err.details}")
finam_trade_api.exceptions.FinamTradeApiError: code=16 | message=Api token could not be verified | details=[]
~/workspace$ python3 examples/account.py
Traceback (most recent call last):
  File "/home/runner/workspace/examples/account.py", line 34, in <module>
    asyncio.run(main())
  File "/nix/store/7d088dip86hlzri9sk0h78b63yfmx0a0-python3-3.11.13/lib/python3.11/asyncio/runners.py", line 190, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/nix/store/7d088dip86hlzri9sk0h78b63yfmx0a0-python3-3.11.13/lib/python3.11/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/nix/store/7d088dip86hlzri9sk0h78b63yfmx0a0-python3-3.11.13/lib/python3.11/asyncio/base_events.py", line 654, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/home/runner/workspace/examples/account.py", line 16, in main
    pprint(await client.account.get_account_info(account_id))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/workspace/finam_trade_api/account/account.py", line 55, in get_account_info
    raise FinamTradeApiError(f"code={err.code} | message={err.message} | details={err.details}")
finam_trade_api.exceptions.FinamTradeApiError: code=5 | message=Account with id None is not found | details=[]