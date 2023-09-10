# SensorSync

![sensorsync](https://github.com/NirajPatel07/SensorSync/assets/66070865/3de20394-b0a3-45f9-9727-d2ef3ae9f66d)

## 1. Introduction

SensorSync is a comprehensive system designed to simulate sensor behavior, monitor sensor readings, and provide APIs for retrieving data based on specific criteria. This project is useful for scenarios where you need to collect, store, and access sensor data, such as temperature and humidity readings, in real-time.

## 2. Project Sections

SensorSync is organized into seven distinct sections, each serving a specific purpose:

### Step 1: Set Up the MQTT Broker with Mosquitto

In this step, we deploy a Mosquitto MQTT broker using Docker. The MQTT broker acts as a message broker that facilitates communication between sensors and clients.

### Step 2: Create MQTT Publisher

Here, we create a Python MQTT client that simulates sensor readings and publishes them to MQTT topics. This emulates the behavior of sensors in a real-world environment.

### Step 3: Create MQTT Subscriber

We construct a Python MQTT subscriber that connects to the MQTT broker, subscribes to topics, and stores received messages in a MongoDB collection. This step facilitates data ingestion from sensors.

### Step 4: Set Up MongoDB

MongoDB is used for data storage. In this step, we set up a MongoDB instance using Docker to store incoming MQTT messages. MongoDB is chosen for its flexibility and scalability.

### Step 5: Implement Redis for In-Memory Data

Redis is used for in-memory data management. We implement Redis using Docker to store the latest ten sensor readings. Redis enables fast data retrieval and caching.

### Step 6: Design FastAPI Endpoints

In this step, we create a FastAPI application with various endpoints to interact with the collected sensor data. FastAPI provides a user-friendly interface for accessing and querying sensor data.

### Step 7: Docker Integration with Docker Compose

To streamline deployment, we integrate all services using Docker Compose. This single configuration file orchestrates the entire system, making it easy to set up and manage.

## 3. Project Directory Structure

![directory](https://github.com/NirajPatel07/SensorSync/assets/66070865/d95c2165-c240-470b-b33a-4c2aa96e1c43)

The project directory structure is organized as follows:

- `MQTT Broker`: Contains the code and Dockerfile for the MQTT broker setup.
- `MQTT_Publisher`: Contains the code for simulating sensor data and publishing it.
- `MQTT_Subscriber`: Contains the code for the MQTT subscriber that stores data in MongoDB.
- `FastAPI_Endpoints`: Contains the FastAPI application code.
- `docker-compose.yml`: Defines the Docker Compose configuration for the entire system.

## 4. Running the Project

To run the project, follow these steps:

1. In the docker-compose.yml file all the paths to create a service docker image are mentioned.

2. Run the Docker Compose configuration to start all services:
   ```docker-compose up ```
   
   ![docker compose run](https://github.com/NirajPatel07/SensorSync/assets/66070865/a40af1b5-3fea-4c20-adee-f0a16d5650ae)
   
This command will bring up all containers, including the MQTT broker, MQTT publisher, MQTT subscriber, MongoDB, Redis, and the FastAPI application.

![docker container](https://github.com/NirajPatel07/SensorSync/assets/66070865/f2d56eae-3e0a-45cc-9105-9fe6e36ff9e8)

Once all services are running, you can access the FastAPI application using the following URL:

```http://127.0.0.1:8000/docs```

![fastapi homepage](https://github.com/NirajPatel07/SensorSync/assets/66070865/8e73e889-7181-4932-9e99-c7be26e3a902)

Here, you'll find the API documentation with details on how to use the available endpoints to fetch sensor readings and access sensor data.

## Sensor Readings:

![sensor read](https://github.com/NirajPatel07/SensorSync/assets/66070865/90c97d13-c0d8-4d29-be14-e343a9b09d0a)

```/sensor-readings/```: Fetch sensor readings within a specified date range.

### Output:

![sensor read op](https://github.com/NirajPatel07/SensorSync/assets/66070865/12323dc4-6635-44cf-8d98-f6ba6eebfe1b)

## Last Ten Reading:

![last ten read](https://github.com/NirajPatel07/SensorSync/assets/66070865/22e42765-26d9-47fa-a682-53cc7e456c24)

```/last-ten-readings/```: Retrieve the last ten sensor readings for a specific sensor.

### Output:

![last ten op](https://github.com/NirajPatel07/SensorSync/assets/66070865/565d9de7-073b-4924-b175-3c7fb0b93139)

Explore the API endpoints and use them as needed to monitor and retrieve sensor data.

Feel free to explore each section of the project to gain a deeper understanding of its functionality and implementation.
