#!/usr/bin/env python3

import json
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validation(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with \"AC\" (Alien Contact)"
            )
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (>7.0) should include received message"
            )
        return self


def get_contacts(*args) -> list:
    contacts = [{
        "contact_id": "AC_2024_001",
        "timestamp": datetime.today(),
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": True
    }]

    for filename in args:
        try:
            with open(filename) as f:
                data = json.load(f)
                if isinstance(data, list):
                    contacts.extend(data)
        except FileNotFoundError:
            print(f"'{filename}' not found, skipping...\n")
        except json.JSONDecodeError:
            print("Error parsing json file, skipping...\n")

        return contacts


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================\n")

    contacts = get_contacts("alien_contacts.json", "invalid_contacts.json")
    for c in contacts:
        try:
            contact = AlienContact(**c)

            print("Valid contact report:")
            print("ID:       ", contact.contact_id)
            print("Type:     ", contact.contact_type.value)
            print("Location: ", contact.location)
            print(f"Signal:    {contact.signal_strength}/10")
            print(f"Duration:  {contact.duration_minutes} minutes")
            print("Witnesses:", contact.witness_count)
            print("Message:  ", (f"\"{contact.message_received}\""
                                 if contact.message_received else None))
            print()

        except ValidationError as e:
            print(f"Error analyzing contact {c.get('contact_id')}:",
                  e.errors()[0]['msg'].replace("Value error, ", ""))
            print()

    print("========================================")
    print("Expected validation error:")

    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.today(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
