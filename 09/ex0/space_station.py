#!/usr/bin/env python3

import json
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(max_length=200)


def get_stations(*args) -> list:
    stations = [{
        "station_id": "ISS01",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": datetime.today(),
        "is_operational": True,
        "notes": None
    }]

    for filename in args:
        try:
            with open(filename) as f:
                data = json.load(f)
                if isinstance(data, list):
                    stations.extend(data)
        except FileNotFoundError:
            print(f"'{filename}' not found, skipping...\n")
        except json.JSONDecodeError:
            print("Error parsing json file, skipping...\n")

    return stations


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    stations = get_stations("space_stations.json", "invalid_stations.json")
    for s in stations:
        try:
            station = SpaceStation(**s)

            print("Valid station created:")
            print("ID:      ", station.station_id)
            print("Name:    ", station.name)
            print("Crew:    ", station.crew_size,
                  "person" if station.crew_size == 1 else "people")
            print(f"Power:    {station.power_level}%")
            print(f"Oxygen:   {station.oxygen_level}%")
            print("Status:  ",
                  ("Operational" if station.is_operational
                   else "Not operational"))
            print()

        except ValidationError as e:
            print(f"Error creating station {s.get('station_id')}:",
                  e.errors()[0]['msg'].replace("Value error, ", ""))
            print()

    print("========================================")
    print("Expected validation error:")

    try:
        SpaceStation(station_id="ISS001",
                     name="International Space Station",
                     crew_size=21,
                     power_level=85.5,
                     oxygen_level=92.3,
                     last_maintenance=datetime.today(),
                     is_operational=True,
                     notes=None)
    except ValidationError as e:
        print(e.errors()[0]['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
