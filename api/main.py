from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello from Docker Compose!",
        "database_url": os.getenv("DATABASE_URL", "not set")
    }

@app.get("/health")
def health():
    return {"status": "ok"}