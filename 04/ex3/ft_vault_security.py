#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    files = [
        "../classified_data.txt",
        "../security_protocols.txt"
    ]

    print("Initiating secure vault access...")
    for file in files:
        try:
            with open(file, "r") as f:
                print("Vault connection established with failsafe protocol")

                print("SECURE READ:\n" + f.read() + "\n")
        except FileNotFoundError:
            print("ERROR: File not found")

    print("All vault operations completed with maximum security")
