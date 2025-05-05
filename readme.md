#  Disaster Communication Privacy-Protected MQTT Simulation

##  Overview

This project simulates a **privacy-aware real-time messaging system** designed for disaster scenarios. It uses **MQTT** to facilitate communication between victims, drones (acting as brokers), and a Command and Control (C2) center.

You will simulate messages using MQTT, identify privacy threats via the **LINDDUN framework**, and apply **Privacy Enhancing Technologies (PETs)** to safeguard sensitive user data.

---

##  Tools & Libraries Used

| Tool / Library       | Purpose                                      |
|----------------------|----------------------------------------------|
| **Mosquitto**        | MQTT broker for publishing/subscribing       |
| **paho-mqtt**        | Python MQTT client library                   |
| **cryptography**     | Encrypt and decrypt MQTT payloads            |
| **hashlib (SHA-256)**| Pseudonymize user IDs and obfuscate topics   |
| **json**, `random`   | JSON message handling and simulation         |

---

##  Installation Guide

### 1.  Install Homebrew (macOS only)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
## Install Mosquito Broker
brew install mosquitto
brew services start mosquitto

## Setup python Virtual Environment 
python3 -m venv ~/mqtt_env
source ~/mqtt_env/bin/activate

## Install Python Dependencies
pip install --upgrade pip
pip install paho-mqtt cryptography

# Step by Step Guide
#### Start the MQTT Broker

brew services start mosquitto

### Run the Basic Subscriber
source ~/mqtt_env/bin/activate
python3 subscriber.py

### Run the Basic Publisher (New Terminal)
source ~/mqtt_env/bin/activate
python3 publisher.py

# PET-Enhanced Execution PETs applied:

Encrypted Payloads with AES (Fernet)

Topic Obfuscation (SHA-256)

Pseudonymization of user_id

Data Minimization (remove unnecessary metadata)

## Run secure Subscriber
source ~/mqtt_env/bin/activate
python3 secure_subscriber.py

## Run Secure Publisher (New Terminal)
source ~/mqtt_env/bin/activate
python3 secure_publisher.py

Encrypted, minimal, and pseudonymized messages are now transmitted after this.

# Interpreting the Results

| Criteria               | Basic System           | With PETs                    |
| ---------------------- | ---------------------- | ---------------------------- |
| Payload encryption     | No                   |  Yes (Fernet)               |
| User identity exposed? |  Yes                  |  No (pseudonymized)         |
| Topic human-readable?  |  Yes  |  No (SHA-256 hash)          |
| Payload fields         | Full                   | Minimal  |
| Privacy risk           |  High                |  Reduced                   |

# Message Format Comparison
### Without PETs
{
  "user_id": "dv_02",
  "location": "35.8044,-122.2711",
  "message": "I need a boat!",
  "device_id": "Google"
}

### With PETs
{
  "id": "2c96c9b4d3f8...",
  "loc": "35.8044,-122.2711",
  "msg": "I need a boat!"
}

# Threat Model - LINDDUN Analysis
| Threat              | Mitigation Applied                      |
| ------------------- | --------------------------------------- |
| **Linkability**     | Topic name obfuscation (SHA-256)        |
| **Identifiability** | Pseudonymized user ID (SHA-256)         |
| **Detectability**   | Payload encryption (Fernet)             |
| **Disclosure**      | Data minimization + encryption          |
| **Unawareness**     | Not covered in current implementation   |
| **Non-compliance**  | Depends on adherence to regulations     |
| **Non-repudiation** | Not implemented (requires logging/sign) |

# Author
Saugat Gautam   
G01536732   
Cyber Security Engineering  
George Mason University
