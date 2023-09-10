import paho.mqtt.client as mqtt
import json
import pymongo
from pymongo import MongoClient
import redis

# MQTT broker configuration
broker_address = "host.docker.internal"
broker_port = 1883

# MQTT topics to subscribe to
temperature_topic = "sensors/temperature"
humidity_topic = "sensors/humidity"

# MongoDB configuration
mongo_host = "mongodb"
mongo_port = 27017  # MongoDB port

# Redis configuration
redis_host = "redis"
redis_port = 6379  # Redis port
redis_list_key = "latest_readings"
max_readings = 10  # Maximum number of readings to store in Redis


# Function to handle MQTT messages
def on_message(client, userdata, message):
    print("\n\n")
    payload = json.loads(message.payload.decode())
    print('payload', payload)
    topic = message.topic
    print(f"Received message on topic '{topic}': {payload}")

    # Store the message in Redis
    store_in_redis(payload)

    # Save the message to MongoDB
    save_to_mongodb(payload)
    print("\n\n")


# Function to save MQTT messages to MongoDB
def save_to_mongodb(data):
    client = MongoClient(mongo_host, mongo_port)
    db = client.mqtt_data
    collection = db.sensor_data

    # Insert the data into the MongoDB collection
    collection.insert_one(data)
    print("Sensor Data saved to MongoDB")


# Function to store MQTT messages in Redis
def store_in_redis(data):
    r = redis.Redis(host=redis_host, port=redis_port)
    print('redis', data)
    # Push the latest reading to the Redis list
    r.lpush(redis_list_key, json.dumps(data))

    # Trim the list to keep only the latest max_readings
    r.ltrim(redis_list_key, 0, max_readings - 1)

    print(f"Sensor Data stored in Redis ({redis_list_key})")


# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to MQTT topics
client.subscribe(temperature_topic)
client.subscribe(humidity_topic)

# Set the message callback
client.on_message = on_message

# Start the MQTT loop to listen for messages
client.loop_forever()
