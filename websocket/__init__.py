"""Local websocket package for the app.

Note: there is a third-party `websocket` package installed in the environment.
This `__init__.py` ensures our local `websocket/` directory is treated as a
Python package so `from websocket.socket_events import ...` resolves correctly.
"""

