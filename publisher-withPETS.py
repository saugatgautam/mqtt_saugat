import paho.mqtt.client as mqtt
import time
import json
import hashlib
import random
#import base64
from cryptography.fernet import Fernet

# MQTT Secure Broker Config
BROKER = "localhost"
PORT = 8883  # TLS port
BASE_TOPIC = "disaster/alerts"

#  for sake of demo the key is hardcoded and shared encryption key to subscriber
key = b'cSiH_xCt6sWto35WALxo696uZlG0dXEijl53o9bvYU4='   
cipher = Fernet(key)

print(f"[KEY] Shared encryption key: {key.decode()}")  

#  message data
raw_messages = [
    {"user_id": "dv_01", "location": "44.9090,-452.6600", "message": "I am here at the basement","device_id": "Apple",},
    {"user_id": "dv_02", "location": "35.8044,-122.2711", "message": "I need a boat!","device_id": "Google",},
    {"user_id": "dv_03", "location": "68.7600,-122.4477", "message": "My childrens are in trouble","device_id": "Oppo",},
]

# PET: Tokenize user ID using SHA-256
def tokenize_user_id(uid):
    return hashlib.sha256(uid.encode()).hexdigest()

# PET: Obfuscate topic name using SHA-256
def obfuscate_topic(topic):
    return hashlib.sha256(topic.encode()).hexdigest()

# PET: Minimize payload fields
def create_minimized_payload(msg):
    return {
        "id": tokenize_user_id(msg["user_id"]),
        "loc": msg["location"],
        "msg": msg["message"]
    }

# MQTT Connect Callback
def on_connect(client, userdata, flags, rc):
    print(f"[INFO] Connected with result code {rc}")

# Create client and configure TLS
client = mqtt.Client()
client.on_connect = on_connect
#client.tls_set()             The tls implemmentation requires certificates, hence the comment
client.connect(BROKER, 1883, 60)  # The tls port is 8883 but for demo sake I used 1883
client.loop_start()

TOPIC = obfuscate_topic(BASE_TOPIC)

try:
    while True:
        original = random.choice(raw_messages)
        minimized = create_minimized_payload(original)
        encrypted_payload = cipher.encrypt(json.dumps(minimized).encode())
        result = client.publish(TOPIC, encrypted_payload)
        if result[0] == 0:
            print(f"[PUBLISH] Sent encrypted to topic {TOPIC}")
        else:
            print("[ERROR] Publish failed")
        time.sleep(5)
except KeyboardInterrupt:
    print("\n[INFO] Publisher stopped.")
    client.loop_stop()