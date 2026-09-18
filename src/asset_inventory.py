"""
Cybersecurity Asset Inventory System
--------------------------------------
A simple CLI application to add, search, update, delete, and display
an organization's IT assets, classified by type and security risk level.

Data is persisted to data/assets.json so it survives between runs.
"""

import json
import os

# ---------------------------------------------------------------------------
# Constants / Valid Choices
# ---------------------------------------------------------------------------

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "assets.json")


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------

def load_assets():
    """Load assets from the JSON data file. Returns an empty list if missing."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_assets(assets):
    """Save the current list of assets back to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# ---------------------------------------------------------------------------
# Input validation helpers
# ---------------------------------------------------------------------------

def get_valid_choice(prompt, choices):
    """Repeatedly prompt until the user enters one of the valid choices
    (case-insensitive), then return the canonically-cased value."""
    choice_map = {c.lower(): c for c in choices}
    while True:
        value = input(f"{prompt} ({'/'.join(choices)}): ").strip()
        if value.lower() in choice_map:
            return choice_map[value.lower()]
        print(f"  Invalid choice. Please choose one of: {', '.join(choices)}")


def get_non_empty(prompt):
    """Repeatedly prompt until the user enters a non-blank value."""
    while True:
        value = input(f"{prompt}: ").strip()
        if value:
            return value
        print("  This field cannot be empty. Please try again.")


def asset_id_exists(assets, asset_id):
    return any(a["asset_id"].lower() == asset_id.lower() for a in assets)


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------

def add_asset(assets):
    print("\n--- Add New Asset ---")

    while True:
        asset_id = get_non_empty("Asset ID")
        if asset_id_exists(assets, asset_id):
            print(f"  Asset ID '{asset_id}' already exists. Please use a unique ID.")
            continue
        break

    asset_name = get_non_empty("Asset Name")
    asset_type = get_valid_choice("Asset Type", ASSET_TYPES)
    ip_address = get_non_empty("IP Address")
    os_name = get_non_empty("Operating System")
    department = get_non_empty("Owner/Department")
    risk_level = get_valid_choice("Risk Level", RISK_LEVELS)
    security_status = get_valid_choice("Security Status", SECURITY_STATUSES)

    asset = {
        "asset_id": asset_id,
        "asset_name": asset_name,
        "asset_type": asset_type,
        "ip_address": ip_address,
        "os": os_name,
        "department": department,
        "risk_level": risk_level,
        "security_status": security_status,
    }

    assets.append(asset)
    save_assets(assets)
    print(f"\n Asset '{asset_id}' added successfully.")


def add_multiple_assets(assets):
    """Bulk-entry mode matching the sample input style (Enter number of assets)."""
    while True:
        try:
            count = int(input("Enter number of assets: ").strip())
            if count <= 0:
                print("  Please enter a positive number.")
                continue
            break
        except ValueError:
            print("  Please enter a valid integer.")

    for i in range(1, count + 1):
        print(f"\nAsset {i}")
        add_asset(assets)


def find_asset_index(assets, asset_id):
    for idx, a in enumerate(assets):
        if a["asset_id"].lower() == asset_id.lower():
            return idx
    return -1


def search_asset(assets):
    print("\n--- Search Asset ---")
    asset_id = get_non_empty("Enter Asset ID to search")
    idx = find_asset_index(assets, asset_id)
    if idx == -1:
        print(f"  No asset found with ID '{asset_id}'.")
        return
    print("\nAsset Found:")
    print_asset(assets[idx])


def update_asset(assets):
    print("\n--- Update Asset ---")
    asset_id = get_non_empty("Enter Asset ID to update")
    idx = find_asset_index(assets, asset_id)
    if idx == -1:
        print(f"  No asset found with ID '{asset_id}'.")
        return

    asset = assets[idx]
    print("Leave a field blank to keep its current value.")

    new_name = input(f"Asset Name [{asset['asset_name']}]: ").strip()
    if new_name:
        asset["asset_name"] = new_name

    new_type = input(f"Asset Type [{asset['asset_type']}] ({'/'.join(ASSET_TYPES)}): ").strip()
    if new_type:
        if new_type.title() in ASSET_TYPES or new_type.capitalize() in ASSET_TYPES:
            match = next((t for t in ASSET_TYPES if t.lower() == new_type.lower()), None)
            asset["asset_type"] = match if match else asset["asset_type"]
        else:
            print("  Invalid type, keeping previous value.")

    new_ip = input(f"IP Address [{asset['ip_address']}]: ").strip()
    if new_ip:
        asset["ip_address"] = new_ip

    new_os = input(f"Operating System [{asset['os']}]: ").strip()
    if new_os:
        asset["os"] = new_os

    new_dept = input(f"Owner/Department [{asset['department']}]: ").strip()
    if new_dept:
        asset["department"] = new_dept

    new_risk = input(f"Risk Level [{asset['risk_level']}] ({'/'.join(RISK_LEVELS)}): ").strip()
    if new_risk:
        match = next((r for r in RISK_LEVELS if r.lower() == new_risk.lower()), None)
        if match:
            asset["risk_level"] = match
        else:
            print("  Invalid risk level, keeping previous value.")

    new_status = input(f"Security Status [{asset['security_status']}] ({'/'.join(SECURITY_STATUSES)}): ").strip()
    if new_status:
        match = next((s for s in SECURITY_STATUSES if s.lower() == new_status.lower()), None)
        if match:
            asset["security_status"] = match
        else:
            print("  Invalid status, keeping previous value.")

    assets[idx] = asset
    save_assets(assets)
    print(f"\n Asset '{asset_id}' updated successfully.")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    asset_id = get_non_empty("Enter Asset ID to delete")
    idx = find_asset_index(assets, asset_id)
    if idx == -1:
        print(f"  No asset found with ID '{asset_id}'.")
        return
    confirm = input(f"Are you sure you want to delete '{asset_id}'? (y/n): ").strip().lower()
    if confirm == "y":
        removed = assets.pop(idx)
        save_assets(assets)
        print(f"\n Asset '{removed['asset_id']}' deleted successfully.")
    else:
        print("  Deletion cancelled.")


def print_asset(asset):
    print(f"Asset ID        : {asset['asset_id']}")
    print(f"Asset Name      : {asset['asset_name']}")
    print(f"Asset Type      : {asset['asset_type']}")
    print(f"IP Address      : {asset['ip_address']}")
    print(f"OS              : {asset['os']}")
    print(f"Department      : {asset['department']}")
    print(f"Risk Level      : {asset['risk_level']}")
    print(f"Status          : {asset['security_status']}")


def display_assets(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    if not assets:
        print("No assets found.")
    else:
        for i, asset in enumerate(assets):
            print_asset(asset)
            if i != len(assets) - 1:
                print("-----------------------------------------")

    total = len(assets)
    critical = sum(1 for a in assets if a["risk_level"] == "Critical")
    high = sum(1 for a in assets if a["risk_level"] == "High")
    medium = sum(1 for a in assets if a["risk_level"] == "Medium")
    vulnerable = sum(1 for a in assets if a["security_status"] == "Vulnerable")

    print("=========================================")
    print(f"Total Assets : {total}")
    print(f"Critical Assets : {critical}")
    print(f"High Risk Assets : {high}")
    print(f"Medium Risk Assets : {medium}")
    print(f"Vulnerable Assets : {vulnerable}")
    print("=========================================")


# ---------------------------------------------------------------------------
# Menu / main loop
# ---------------------------------------------------------------------------

def print_menu():
    print("\n===== CYBERSECURITY ASSET INVENTORY SYSTEM =====")
    print("1. Add Asset")
    print("2. Add Multiple Assets (bulk entry)")
    print("3. Search Asset")
    print("4. Update Asset")
    print("5. Delete Asset")
    print("6. Display All Assets & Security Summary")
    print("7. Exit")


def main():
    assets = load_assets()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            add_multiple_assets(assets)
        elif choice == "3":
            search_asset(assets)
        elif choice == "4":
            update_asset(assets)
        elif choice == "5":
            delete_asset(assets)
        elif choice == "6":
            display_assets(assets)
        elif choice == "7":
            print("\nExiting... Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
