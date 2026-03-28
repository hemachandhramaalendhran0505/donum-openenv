import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from env.donum_env import DonumEnv
from env.models import Action
from grader.grader_basic import compute_score

env = DonumEnv()

obs = env.reset("easy")

print("\n===== INITIAL OBSERVATION =====")
print(obs)

action = Action(
    donation_id=0,
    ngo_id=0,
    volunteer_id=0
)

obs, reward, done, _ = env.step(action)

print("\n===== AFTER STEP =====")
print("Observation:", obs)
print("Reward:", reward)
print("Done:", done)

score = compute_score(env)

print("\n===== FINAL SCORE =====")
print(score)