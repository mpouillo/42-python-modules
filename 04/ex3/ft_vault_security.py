#!/usr/bin/env python3

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocol")

    try:
        with open("classified_data.txt", "r") as f:
            print("\nSECURE EXTRACTION:")
            print(f.read())

        with open("security_protocols.txt", "w") as f:
            print("\nSECURE PRESERVATION:")
            print("[CLASSIFIED] New security protocols archived")
            f.write("[CLASSIFIED] New security protocols archived")

    except FileNotFoundError:
        print("ERROR: File not found")
    finally:
        print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security")
