from fastapi import FastAPI
import redis  # ✅ Required import

app = FastAPI()

# Connect to Redis (Docker Compose service name)
r = redis.Redis(host='redis', port=6379, db=0)

@app.get("/")
def read_root():
    # Set and get a message in Redis
    r.set("message", "Hello from FastAPI via Redis!")
    msg = r.get("message")
    return {"message_from_redis": msg.decode()}
