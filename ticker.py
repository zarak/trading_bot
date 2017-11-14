import websocket


def on_message(ws, message):
    msg = pd.read_json(message)
    print(msg.events.iloc[0]['price'])


ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/BTCUSD", on_message=on_message)
ws.run_forever(ping_interval=5)
