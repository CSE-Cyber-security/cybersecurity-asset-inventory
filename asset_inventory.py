assets = []

def add_asset():
    asset = {
        "id": input("Asset ID: "),
        "name": input("Asset Name: "),
        "type": input("Asset Type: "),
        "ip": input("IP Address: "),
        "os": input("Operating System: "),
        "department": input("Owner/Department: "),
        "risk": input("Risk Level: "),
        "status": input("Security Status: ")
    }

    assets.append(asset)
    print("Asset added successfully!")


def display_assets():
    print("\n=========================================")
    print("      CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    for asset in assets:
        print("Asset ID :", asset["id"])
        print("Asset Name :", asset["name"])
        print("Asset Type :", asset["type"])
        print("IP Address :", asset["ip"])
        print("OS :", asset["os"])
        print("Department :", asset["department"])
        print("Risk Level :", asset["risk"])
        print("Status :", asset["status"])
        print("-----------------------------------------")


def search_asset():
    search_id = input("Enter Asset ID to search: ")

    for asset in assets:
        if asset["id"] == search_id:
            print("\nAsset Found!")
            for key, value in asset.items():
                print(key, ":", value)
            return

    print("Asset not found.")


def update_asset():
    update_id = input("Enter Asset ID to update: ")

    for asset in assets:
        if asset["id"] == update_id:
            asset["name"] = input("New Asset Name: ")
            asset["type"] = input("New Asset Type: ")
            asset["ip"] = input("New IP Address: ")
            asset["os"] = input("New Operating System: ")
            asset["department"] = input("New Department: ")
            asset["risk"] = input("New Risk Level: ")
            asset["status"] = input("New Security Status: ")

            print("Asset updated successfully!")
            return

    print("Asset not found.")


def delete_asset():
    delete_id = input("Enter Asset ID to delete: ")

    for asset in assets:
        if asset["id"] == delete_id:
            assets.remove(asset)
            print("Asset deleted successfully!")
            return

    print("Asset not found.")


while True:

    print("\n===== CYBERSECURITY ASSET INVENTORY =====")
    print("1. Add Asset")
    print("2. Search Asset")
    print("3. Update Asset")
    print("4. Delete Asset")
    print("5. Display Assets")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_asset()

    elif choice == "2":
        search_asset()

    elif choice == "3":
        update_asset()

    elif choice == "4":
        delete_asset()

    elif choice == "5":
        display_assets()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")