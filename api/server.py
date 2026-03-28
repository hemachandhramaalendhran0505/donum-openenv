from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dummy state
state = {
    "donations": [],
    "ngos": [],
    "volunteers": [],
    "time_step": 0
}

# Request model
class Action(BaseModel):
    donation_id: int = 0
    ngo_id: int = 0
    volunteer_id: int = 0

@app.get("/")
def root():
    return {"message": "Donum OpenEnv running"}

# ✅ RESET endpoint (IMPORTANT)
@app.post("/reset")
def reset():
    global state
    state = {
        "donations": [],
        "ngos": [],
        "volunteers": [],
        "time_step": 0
    }
    return state

# ✅ STEP endpoint
@app.post("/step")
def step(action: Action):
    global state
    state["time_step"] += 1

    return {
        "observation": state,
        "reward": 1.0,
        "done": False,
        "info": {"message": "Step executed"}
    }

# ✅ STATUS endpoint
@app.get("/status")
def status():
    return state