import time
import random
import json
from datetime import datetime

import paho.mqtt.client as mqtt


broker = "test.mosquitto.org"
port = 1883
topic = "rojda_digital_twin_office_2026"


client = mqtt.Client()
client.connect(broker, port, 60)

while True:
    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "room": random.choice(["Meeting Room", "Open Office"]),
        "temperature": random.randint(20, 30),
        "energy_kwh": round(random.uniform(0.1, 3.0), 2)
    }

    message = json.dumps(data)

    client.publish(topic, message)

    print("Published:", message)

    time.sleep(3)


  