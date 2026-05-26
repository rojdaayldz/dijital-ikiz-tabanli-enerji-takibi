import json
import csv
import os

import paho.mqtt.client as mqtt


broker = "test.mosquitto.org"
port = 1883
topic = "rojda_digital_twin_office_2026"
csv_file = "iot_energy_log.csv"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code:", rc)
    client.subscribe(topic)
    print("Subscribed to topic:", topic)


def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    file_exists = os.path.exists(csv_file)

    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["time", "room", "temperature", "energy_kwh"])

        writer.writerow([
            data["time"],
            data["room"],
            data["temperature"],
            data["energy_kwh"]
        ])

    print("Saved IoT data:", data)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

print("Waiting for IoT data and saving to CSV...")

client.loop_forever()