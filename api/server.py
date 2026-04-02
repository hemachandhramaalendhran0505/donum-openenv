from fastapi import FastAPI, Body, Request
from env.donum_env import DonumEnv
from env.models import Action
from grader.grader_basic import compute_score

app = FastAPI()

env = DonumEnv()


# ✅ Health check
@app.get("/health")
def health():
    return {"status": "ok"}


# ✅ REQUIRED: POST reset
@app.post("/reset")
def reset_env(difficulty: str = Body("easy")):
    obs = env.reset(difficulty)
    return obs


# ✅ REQUIRED: POST infer (CRITICAL)
@app.post("/infer")
async def infer(request: Request):
    data = await request.json()

    env.reset("easy")

    action_data = data.get("action", {})

    try:
        action = Action(**action_data)
    except:
        action = Action()

    obs, reward, done, _ = env.step(action)

    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }


# Optional
@app.post("/step")
def step_env(action: Action):
    obs, reward, done, _ = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done
    }


@app.get("/state")
def get_state():
    return env.state()


@app.get("/grader")
def get_score():
    return {"score": compute_score(env)}


@app.get("/")
def root():
    return {"message": "Donum OpenEnv Running"}