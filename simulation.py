import time
import random
import csv
from datetime import datetime

from device import Device
from office import Office


lamp = Device("Lamp", 10, "Meeting Room")
computer = Device("Computer", 120, "Open Office")
air_conditioner = Device("Air Conditioner", 900, "Meeting Room")
printer = Device("Printer", 300, "Open Office")

office = Office("Smart Office")

office.add_device(lamp)
office.add_device(computer)
office.add_device(air_conditioner)
office.add_device(printer)


with open("energy_log.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
    "time",
    "device",
    "room",
    "is_on",
    "usage_hours",
    "energy_kwh",
    "temperature"
])

    for i in range(10):
        print(f"\nSimulation step: {i + 1}")

        for device in office.devices:
            device.is_on = random.choice([True, False])

            usage_hours = random.randint(1, 8)
            device.set_usage_hours(usage_hours)

            energy = device.get_consumption()
            temperature = random.randint(20, 30)

            print(
                f"{device.name} | ON: {device.is_on} | Usage: {usage_hours} hours | Energy: {energy} kWh"
            )

            writer.writerow([
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    device.name,
    device.room,
    device.is_on,
    usage_hours,
    energy,
    temperature
])

        print("Total Energy:", office.total_consumption(), "kWh")

        time.sleep(1)