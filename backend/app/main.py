from fastapi import FastAPI

app = FastAPI(title="CineMatch API", version="0.1.0")


@app.get("/api/saude")
def saude():
    return {"status": "ok", "app": "CineMatch"}