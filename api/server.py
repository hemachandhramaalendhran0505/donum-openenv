from fastapi import FastAPI
from env.donum_env import DonumEnv
from env.models import Action
from grader.grader_basic import compute_score

app = FastAPI()

env = DonumEnv()


@app.get("/reset")
def reset_env(difficulty: str = "easy"):
    obs = env.reset(difficulty)
    return obs


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


@app.get("/tasks")
def get_tasks():
    return ["easy", "medium", "hard"]


@app.get("/grader")
def get_score():
    score = compute_score(env)
    return {"score": score}


@app.get("/")
def root():
    return {"message": "Donum OpenEnv Running"}