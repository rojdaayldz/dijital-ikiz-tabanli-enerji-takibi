import pandas as pd

from sklearn.linear_model import LinearRegression

df = pd.read_csv("energy_log.csv")

X = df[["usage_hours"]]
y = df["energy_kwh"]

model = LinearRegression()

model.fit(X, y)

prediction_input = pd.DataFrame([[5]], columns=["usage_hours"])

predicted_energy = model.predict(prediction_input)

print("Predicted energy consumption for 5 hours:")
print(predicted_energy[0], "kWh")