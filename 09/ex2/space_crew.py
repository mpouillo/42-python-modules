#!/usr/bin/env python3

import json
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from typing import List


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=10)
    mission_status: str = "Planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with \"M\"")

        ranks = [c.rank for c in self.crew]
        if not (Rank.commander in ranks or Rank.captain in ranks):
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            exp_crew = [c for c in self.crew if c.years_experience > 5]
            if (len(exp_crew) / len(self.crew)) < 0.5:
                raise ValueError("Long missions (> 365 days) need "
                                 "50% experienced crew (5+ years)")

        if any(not c.is_active for c in self.crew):
            raise ValueError("All crew members must be active")

        return self


def get_missions(*args) -> list:
    missions = [{
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Williams",
                "rank": "captain",
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": True
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": "captain",
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 30,
                "is_active": True
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": "cadet",
                "age": 35,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True
            },
            {
                "member_id": "CM004",
                "name": "David Smith",
                "rank": "commander",
                "age": 27,
                "specialization": "Security",
                "years_experience": 15,
                "is_active": True
            },
            {
                "member_id": "CM005",
                "name": "Maria Jones",
                "rank": "cadet",
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True
            }
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1
    }]

    for filename in args:
        try:
            with open(filename) as f:
                data = json.load(f)
                if isinstance(data, list):
                    missions.extend(data)
        except FileNotFoundError:
            print(f"'{filename}' not found, skipping...\n")
        except json.JSONDecodeError:
            print("Error parsing json file, skipping...\n")

        return missions


def main() -> None:
    print("Space Mission Crew Validation")
    print("======================================\n")

    missions = get_missions("space_missions.json")
    for m in missions:
        try:
            mission = SpaceMission(**m)
            crew = [CrewMember(**val) for val in m.get("crew")]

            print("Valid mission created:")
            print("Mission:", mission.mission_name)
            print("ID", mission.mission_id)
            print("Destination", mission.destination)
            print("Duration", mission.duration_days)
            print("Budget", mission.budget_millions)
            print("Crew size", len(mission.crew))
            print("Crew members:")
            print("\n".join(f"- {c.name} ({c.rank.value}) - {c.specialization}"
                            for c in mission.crew))
            print()

        except ValidationError as e:
            print(f"Error creating mission {m.get('mission_id')}:",
                  e.errors()[0]['msg'].replace("Value error, ", ""))
            print()

    print("========================================")
    print("Expected validation error:")

    try:
        crew = [
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.lieutenant,
                age=43,
                specialization="Mopping",
                years_experience=19,
                is_active=True
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.lieutenant,
                age=43,
                specialization="Navigation",
                years_experience=12,
                is_active=True
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.officer,
                age=37,
                specialization="Engineering",
                years_experience=10,
                is_active=True
            )
        ]

        SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=crew,
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
