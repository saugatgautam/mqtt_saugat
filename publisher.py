import paho.mqtt.client as mqtt
import time
import json
import random



# victim message contents
messages = [
    {"user_id": "dv_01", "location": "44.9090,-452.6600", "message": "I am here at the basement","device_id": "Apple",},
    {"user_id": "dv_02", "location": "35.8044,-122.2711", "message": "I need a boat!","device_id": "Google",},
    {"user_id": "dv_03", "location": "68.7600,-122.4477", "message": "My childrens are in trouble","device_id": "Oppo",},
]

BROKER = "localhost"
PORT = 1883
TOPIC = "disaster/alerts"

def on_connect(client, userdata, flags, rc):
    print(f"[INFO] Connected with result code {rc}")

client = mqtt.Client()        # create client to send message
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)
client.loop_start()

try:                 # the publisher continues sending messages 
    while True:
        msg = random.choice(messages)
        payload = json.dumps(msg)
        result = client.publish(TOPIC, payload)
        if result[0] == 0:
            print(f"[PUBLISH] Sent: {payload}")
        else:
            print("[ERROR] Failed to send message")
        time.sleep(5)
        
except KeyboardInterrupt:
    print("\n[INFO] Publisher stopped.")
    client.loop_stop()