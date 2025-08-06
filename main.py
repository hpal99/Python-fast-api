from fastapi import FastAPI # pyright: ignore[reportMissingImports]
import ls # type: ignore

app = FastAPI()

# Connect to Redis (service name from docker-compose.yml)
r = redis.Redis(host='redis', port=6379, db=0) # pyright: ignore[reportUndefinedVariable]

@app.get("/")
def read_root():
    # Simple Redis interaction
    r.set("message", "Hello from FastAPI via Redis!")
    msg = r.get("message")
    return {"message_from_redis": msg.decode()}
