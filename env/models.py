from pydantic import BaseModel
from typing import List


class Donation(BaseModel):
    id: int
    quantity: int
    expiry_time: int
    x: float
    y: float


class NGO(BaseModel):
    id: int
    demand: int
    priority: int
    x: float
    y: float


class Volunteer(BaseModel):
    id: int
    available: bool
    x: float
    y: float


class Observation(BaseModel):
    donations: List[Donation]
    ngos: List[NGO]
    volunteers: List[Volunteer]
    time_step: int


class Action(BaseModel):
    donation_id: int
    ngo_id: int
    volunteer_id: int


class Reward(BaseModel):
    value: float
    reason: str