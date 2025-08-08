from fastapi import FastAPI # pyright: ignore[reportMissingImports]
import redis # pyright: ignore[reportMissingImports]

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    try:
        r = redis.Redis(host="redis", port=6379, decode_responses=True)
        if r.ping():
            return {"status": "ok", "redis": "connected"}
    except redis.exceptions.ConnectionError:
        return {"status": "ok", "redis": "unreachable"}  # Still OK for app health

    return {"status": "error"}
