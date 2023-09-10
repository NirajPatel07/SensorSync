import json
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
import redis
from fastapi.openapi.models import Info, ExternalDocumentation, Contact, License
from fastapi.openapi.models import OpenAPI
from fastapi.openapi.models import Tag

# Create a FastAPI instance
app = FastAPI(
    title="SensorSync",
    description="API for sensor data management",
    version="1.0.0"
)

# MongoDB configuration
mongo_host = "localhost"
mongo_port = 27017
mongo_db_name = "mqtt_data"
mongo_collection_name = "sensor_data"

# Redis configuration
redis_host = "localhost"
redis_port = 6379

# Connect to MongoDB
mongo_client = MongoClient(host=mongo_host, port=mongo_port)
mongo_db = mongo_client.mqtt_data
mongo_collection = mongo_db.sensor_data

# Connect to Redis
redis_client = redis.Redis(host=redis_host, port=redis_port)
redis_list_key = "latest_readings"


# Endpoint to fetch sensor readings by specifying a start and end range
@app.get("/sensor-readings/", tags=["Sensor Readings"])
async def get_sensor_readings(start_date, end_date):
    try:
        # Query MongoDB for sensor readings within the specified date range
        sensor_readings = mongo_collection.find({
            "timestamp": {"$gte": start_date, "$lte": end_date}
        })

        response = []
        for reading in sensor_readings:
            curr_reading = {}
            curr_reading['sensor_id'] = reading['sensor_id']
            curr_reading['value'] = reading['value']
            curr_reading['timestamp'] = reading['timestamp']
            response.append(curr_reading)

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


# Endpoint to retrieve the last ten sensor readings for a specific sensor
@app.get("/last-ten-readings/", tags=["Last Ten Readings"])
async def get_last_ten_readings():
    try:
        # Retrieve the last ten sensor readings from Redis
        last_ten_readings = redis_client.lrange(redis_list_key, 0, -1)
        return [json.loads(reading.decode('utf-8')) for reading in last_ten_readings]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
