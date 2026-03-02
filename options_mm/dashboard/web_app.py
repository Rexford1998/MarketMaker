from fastapi import FastAPI

app = FastAPI(title="Options MM Dashboard")


@app.get("/health")
def health():
    return {"status": "ok"}
