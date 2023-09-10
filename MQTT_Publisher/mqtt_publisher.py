import paho.mqtt.client as mqtt
import json
import random
import time

# MQTT broker configuration
broker_address = "host.docker.internal"
broker_port = 1883  # MQTT broker port

# MQTT topics
temperature_topic = "sensors/temperature"
humidity_topic = "sensors/humidity"


# Function to generate simulated sensor data
def generate_sensor_data(sensor_id):
    value = round(random.uniform(20.0, 30.0), 2)  # Simulate a value between 20.0 and 30.0
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sensor_data = {
        "sensor_id": sensor_id,
        "value": value,
        "timestamp": timestamp
    }
    return json.dumps(sensor_data)


# Create an MQTT client
client = mqtt.Client("admin")

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

try:
    while True:
        # Simulate sensor readings
        temperature_data = generate_sensor_data("temperature_sensor")
        humidity_data = generate_sensor_data("humidity_sensor")

        # Publish sensor data to MQTT topics
        client.publish(temperature_topic, temperature_data)
        client.publish(humidity_topic, humidity_data)

        print(f"Published: {temperature_topic} - {temperature_data}")
        print(f"Published: {humidity_topic} - {humidity_data}")

        time.sleep(2)

except KeyboardInterrupt:
    print("Publisher stopped.")
    client.disconnect()
