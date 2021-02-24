import websocket
from os import getenv

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

if __name__ == "__main__":
    token = getenv("TOKEN", "c0htplv48v6qgpegtbk0")
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={token}",
                                 on_message = on_message,
                                 on_error = on_error,
                                 on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()