#!/usr/bin/env python3

def access_file(filename: str) -> None:
    try:
        with open(filename, "r") as f:
            print(f"ROUTINE ACCESS: Attempting access to {filename}")
            print(f"SUCCESS: Archive recovered - \"{f.read()}\"")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    filenames = [
        "lost_archive.txt",
        "classified_data.txt",
        "standard_archive.txt"
    ]

    for f in filenames:
        access_file(f)
        print()

    print("All crisis scenarios handled successfully. Archives secure.")
