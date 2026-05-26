import pandas as pd

df = pd.read_csv("energy_log.csv")

print("Energy Log Data:")
print(df)

print("\nAverage energy consumption by device:")
print(df.groupby("device")["energy_kwh"].mean())

print("\nTotal energy consumption by device:")
print(df.groupby("device")["energy_kwh"].sum())

print("\nMost consuming device:")
print(df.groupby("device")["energy_kwh"].sum().idxmax())
import matplotlib.pyplot as plt

total_energy = df.groupby("device")["energy_kwh"].sum()

total_energy.plot(kind="bar")

plt.title("Total Energy Consumption by Device")
plt.xlabel("Device")
plt.ylabel("Energy Consumption (kWh)")
plt.tight_layout()
plt.show()