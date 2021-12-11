from websocket import create_connection 
import Adafruit_DHT as dht
import time
import json 

register_message = {
    "type": "register",
    "payload": {
        "name": "abobus",
        "type": "dht"
    }
}

server_url = "ws://192.168.2.37:3000/hub/ws"

ws = create_connection(server_url)
print("Registered with: " + json.dumps(register_message))
ws.send(json.dumps(register_message))

try:
    while True:
        humidity, temperature = dht.read_retry(11, 14)
        data = {
            "type": "data",
            "payload": {
                "humidity": humidity,
                "temperature": temperature
            }
        }
        print(json.dumps(data))
        time.sleep(1)
        ws.send(json.dumps(data))
except:
    print("Error occured")
finally:
    ws.close()
    print("Exiting...")
