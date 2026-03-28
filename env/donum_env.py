import random
import math
from typing import List

from .models import Donation, NGO, Volunteer, Observation, Action, Reward
from .tasks import get_easy_task, get_medium_task, get_hard_task


class DonumEnv:

    def __init__(self):
        self.time_step = 0
        self.max_steps = 10
        self.donations: List[Donation] = []
        self.ngos: List[NGO] = []
        self.volunteers: List[Volunteer] = []

    def reset(self, difficulty="easy"):
        self.time_step = 0

        if difficulty == "easy":
            config = get_easy_task()
        elif difficulty == "medium":
            config = get_medium_task()
        else:
            config = get_hard_task()

        self._generate_fake_data(config)

        return self._get_observation()

    def step(self, action: Action):
        reward_value = self._calculate_reward(action)

        self.time_step += 1
        done = self.time_step >= self.max_steps

        obs = self._get_observation()

        reward = Reward(value=reward_value, reason="step reward")

        return obs, reward, done, {}

    def state(self):
        return {
            "time_step": self.time_step
        }

    def _generate_fake_data(self, config):

        self.donations = [
            Donation(
                id=i,
                quantity=random.randint(5, 20),
                expiry_time=random.randint(5, 50),
                x=random.uniform(0, 100),
                y=random.uniform(0, 100),
            )
            for i in range(config["donations"])
        ]

        self.ngos = [
            NGO(
                id=i,
                demand=random.randint(5, 20),
                priority=random.randint(1, 3),
                x=random.uniform(0, 100),
                y=random.uniform(0, 100),
            )
            for i in range(config["ngos"])
        ]

        self.volunteers = [
            Volunteer(
                id=i,
                available=True,
                x=random.uniform(0, 100),
                y=random.uniform(0, 100),
            )
            for i in range(config["volunteers"])
        ]

    def _get_observation(self):

        return Observation(
            donations=self.donations,
            ngos=self.ngos,
            volunteers=self.volunteers,
            time_step=self.time_step,
        )

    def _distance(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def _calculate_reward(self, action: Action):

        donation = next((d for d in self.donations if d.id == action.donation_id), None)
        ngo = next((n for n in self.ngos if n.id == action.ngo_id), None)
        volunteer = next((v for v in self.volunteers if v.id == action.volunteer_id), None)

        if not donation or not ngo or not volunteer:
            return -1.0

        # Distance score (closer is better)
        dist = self._distance(donation.x, donation.y, ngo.x, ngo.y)
        distance_score = 1 / (1 + dist)

        # Expiry score (lower expiry time → more urgent → higher reward)
        expiry_score = 1 / (1 + donation.expiry_time)

        # Demand matching score
        demand_diff = abs(donation.quantity - ngo.demand)
        demand_score = 1 / (1 + demand_diff)

        # NGO priority score (1–3 → scaled to 0.33–1)
        priority_score = ngo.priority / 3

        # Final weighted reward
        reward = (
            0.4 * distance_score +
            0.2 * expiry_score +
            0.2 * demand_score +
            0.2 * priority_score
        )

        return round(reward, 3)