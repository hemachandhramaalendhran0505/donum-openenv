from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Donum OpenEnv is running 🚀"}

@app.post("/reset")
def reset():
    return {"status": "reset successful"}

@app.post("/step")
def step():
    return {"status": "step executed"}

@app.get("/health")
def health():
    return {"status": "ok"}
