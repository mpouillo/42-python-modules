#!/usr/bin/env python3

if __name__ == "__main__":
    entries = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]

    filename = "new_discovery.txt"

    try:
        print(f"Initializing new storage unit: {filename}")

        f = open(filename, "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")

        for i, e in enumerate(entries):
            string = "[ENTRY " + str(i).zfill(3) + "] " + e + "\n"
            f.write(string)
            print(string, end="")

        f.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")
    except IOError:
        print("ERROR: Could not access storage vault")
