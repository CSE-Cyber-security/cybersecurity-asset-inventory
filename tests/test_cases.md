# Test Cases — Cybersecurity Asset Inventory System

Manual test cases to verify the CLI behaves correctly. Run `python3 src/asset_inventory.py` from the project root and follow each scenario.

| # | Test Case | Steps | Expected Result |
|---|-----------|-------|------------------|
| 1 | Add a single asset | Menu → 1 → fill in valid Asset ID (e.g. A201) and all fields | "Asset 'A201' added successfully." message; asset appears in `data/assets.json` |
| 2 | Add multiple assets (bulk) | Menu → 2 → enter `3` → fill in 3 assets (A101, A102, A103 from sample input) | All 3 assets added; output matches the sample expected output exactly |
| 3 | Reject duplicate Asset ID | Menu → 1 → enter an Asset ID that already exists | Program prints "already exists" and re-prompts for a unique ID |
| 4 | Reject empty required field | Menu → 1 → leave Asset Name blank and press Enter | Program prints "cannot be empty" and re-prompts until a value is given |
| 5 | Reject invalid Asset Type | Menu → 1 → enter Asset Type as "Laptop" | Program prints "Invalid choice" and re-prompts with valid options |
| 6 | Reject invalid Risk Level | Menu → 1 → enter Risk Level as "Severe" | Program prints "Invalid choice" and re-prompts |
| 7 | Reject invalid Security Status | Menu → 1 → enter Security Status as "Broken" | Program prints "Invalid choice" and re-prompts |
| 8 | Search for existing asset | Menu → 3 → enter an Asset ID that exists (e.g. A101) | Full asset details are printed |
| 9 | Search for non-existent asset | Menu → 3 → enter an Asset ID that does not exist (e.g. Z999) | "No asset found with ID 'Z999'." message |
| 10 | Update an existing asset | Menu → 4 → enter A102 → change Risk Level to "Medium", leave others blank | Only Risk Level changes; all other fields stay the same |
| 11 | Update non-existent asset | Menu → 4 → enter Z999 | "No asset found with ID 'Z999'." message |
| 12 | Delete an existing asset, confirm | Menu → 5 → enter A103 → confirm with `y` | Asset removed from list and from `data/assets.json` |
| 13 | Delete an existing asset, cancel | Menu → 5 → enter A103 → cancel with `n` | Asset remains unchanged |
| 14 | Delete non-existent asset | Menu → 5 → enter Z999 | "No asset found with ID 'Z999'." message |
| 15 | Display all assets & summary | Menu → 6 (with 3 sample assets loaded) | Output matches the "Expected Output" format exactly, including correct Total Assets, Critical Assets, High Risk Assets, Medium Risk Assets, and Vulnerable Assets counts |
| 16 | Display with no assets | Menu → 6 (with an empty inventory) | "No assets found." message and all counts show 0 |
| 17 | Data persistence | Add an asset, exit the program (Menu → 7), relaunch the program, Menu → 6 | Previously added asset is still present, loaded from `data/assets.json` |
| 18 | Invalid menu choice | At the main menu, enter `9` | "Invalid choice. Please enter a number from 1 to 7." message, menu re-displays |

## Sample Data Verification

Using the exact sample input from the assignment (A101, A102, A103), the displayed summary must show:

- Total Assets : 3
- Critical Assets : 1
- High Risk Assets : 1
- Medium Risk Assets : 1
- Vulnerable Assets : 1

This was verified against `src/asset_inventory.py` and matches the expected output in the assignment brief exactly.
