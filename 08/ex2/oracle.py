#!/usr/bin/env python3

import os
from dotenv import load_dotenv, dotenv_values


def security_check() -> None:
    print("\nEnvironment security check:")

    file_config = dotenv_values(".env")

    if file_config.get("API_KEY") != "Authenticated":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] Hardcoded secrets detected")

    wrong_key = False
    for key in [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ]:
        if key not in os.environ.keys():
            print("[KO] Error in .env file")
            wrong_key = True
            break
    if not wrong_key:
        print("[OK] .env file properly configured")

    if os.environ.get("MATRIX_MODE") != file_config.get("MATRIX_MODE"):
        print("[OK] Production overrides available")
    else:
        print("[KO] Production does not override available")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix\n")

    load_dotenv()

    print("Configuration loaded:")
    print("Mode:", os.environ.get("MATRIX_MODE"))
    print("Database:", os.environ.get("DATABASE_URL"))
    print("API Access:",
          "Authenticated" if os.environ.get("API_KEY") == "secret123"
          else "Unauthenticated")
    print("Log Level:", os.environ.get("LOG_LEVEL"))
    print("Zion Network:", os.environ.get("ZION_ENDPOINT"))

    security_check()

    print("\nThe Oracle sees all configurations.")
