#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    filename = "../ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vaullt: '{filename}'")
        f = open(filename, "r")
        print("Connection established...\n")
        print(f.read())
        f.close()
        print("\nData recovery complete. Storage unit disconnected")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")
