from streamlit_autorefresh import st_autorefresh
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Digital Twin Dashboard", layout="wide")
st_autorefresh(interval=3000, key="datarefresh")

st.title("Smart Office Digital Twin")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Username or password is incorrect.")

    st.stop()

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

df = pd.read_csv("energy_log.csv")

total_energy = df.groupby("device")["energy_kwh"].sum()
room_energy = df.groupby("room")["energy_kwh"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Devices", len(df["device"].unique()))
col2.metric("Total Energy (kWh)", round(df["energy_kwh"].sum(), 2))
col3.metric("Highest Consumer", total_energy.idxmax())

st.subheader("Energy Consumption Data")
st.dataframe(df)

st.subheader("Total Energy Consumption by Device")
st.bar_chart(total_energy)
st.subheader("Room Based Energy Consumption")
st.bar_chart(room_energy)

st.subheader("Average Energy Consumption")
avg_energy = df.groupby("device")["energy_kwh"].mean()
st.line_chart(avg_energy)
st.subheader("Energy Warning System")

threshold = 5

for device, energy in total_energy.items():
    if energy > threshold:
        st.warning(f"{device} yüksek enerji tüketiyor: {round(energy, 2)} kWh")
    else:
        st.success(f"{device} normal seviyede: {round(energy, 2)} kWh")
        st.subheader("Average Temperature by Room")

room_temperature = df.groupby("room")["temperature"].mean()

st.line_chart(room_temperature)
st.subheader("Temperature Warning System")

temperature_threshold = 27

for room, temperature in room_temperature.items():
    if temperature > temperature_threshold:
        st.warning(f"{room} sıcaklığı yüksek: {round(temperature, 1)} °C")
    else:
        st.success(f"{room} sıcaklığı normal: {round(temperature, 1)} °C")


from sklearn.linear_model import LinearRegression

st.subheader("AI Energy Prediction")

X = df[["usage_hours"]]
y = df["energy_kwh"]

model = LinearRegression()
model.fit(X, y)

selected_hours = st.slider("Select usage hours", 1, 10, 5)

prediction_input = pd.DataFrame([[selected_hours]], columns=["usage_hours"])
predicted_energy = model.predict(prediction_input)

st.write(f"Predicted energy consumption for {selected_hours} hours:")
st.metric("Predicted Energy", f"{round(predicted_energy[0], 2)} kWh") 


st.subheader("Smart HVAC Control System")

season_mode = st.selectbox("Select Season Mode", ["Summer", "Winter"])
target_temperature = st.slider("Target Temperature (°C)", 18, 28, 22)

for room, temperature in room_temperature.items():
    st.write(f"{room} current average temperature: {round(temperature, 1)} °C")

    if season_mode == "Summer":
        if temperature > target_temperature:
            st.warning(f"{room}: Temperature is high. AC should be ON.")
        else:
            st.success(f"{room}: Temperature is comfortable. AC can be OFF.")

    elif season_mode == "Winter":
        if temperature < target_temperature:
            st.warning(f"{room}: Temperature is low. Heater should be ON.")
        else:
            st.success(f"{room}: Temperature is comfortable. Heater can be OFF.")
            import os

st.subheader("Live IoT Data from MQTT")

iot_file = "iot_energy_log.csv"

if os.path.exists(iot_file):

    iot_df = pd.read_csv(iot_file)

    st.write("Latest IoT Sensor Data")
    st.dataframe(iot_df.tail(10))

    st.subheader("IoT Room Temperature")
    iot_room_temp = iot_df.groupby("room")["temperature"].mean()
    st.line_chart(iot_room_temp)

    st.subheader("IoT Room Energy Consumption")
    iot_room_energy = iot_df.groupby("room")["energy_kwh"].sum()
    st.bar_chart(iot_room_energy)

else:
    st.info("No MQTT data received yet.")