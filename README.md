# Week 01 — Cybersecurity Asset Inventory System

A command-line Python application that lets a security administrator add, search, update, delete, and display an organization's IT assets, with automatic classification by asset type and security risk level.

## Problem Statement

Organizations maintain many IT assets — computers, servers, routers, switches, and applications. Managing these manually makes it hard to track security status and identify assets needing urgent attention. This system centralizes that tracking in one place.

## Features

- **Add Asset** — add one asset at a time with full input validation
- **Add Multiple Assets** — bulk entry matching the assignment's sample input flow ("Enter number of assets")
- **Search Asset** — look up an asset by ID
- **Update Asset** — edit any field of an existing asset (blank = keep current value)
- **Delete Asset** — remove an asset, with a confirmation prompt
- **Display All Assets** — prints a formatted inventory report plus a security summary
- **Data persistence** — all changes are saved to `data/assets.json` and reloaded on the next run
- **Input validation** — Asset Type, Risk Level, and Security Status are restricted to their valid options; required fields cannot be blank; duplicate Asset IDs are rejected

## Data Fields

| Field | Description |
|---|---|
| Asset ID | Unique identifier |
| Asset Name | Descriptive name |
| Asset Type | Workstation / Server / Router / Switch / Application |
| IP Address | Asset's network address |
| Operating System | OS running on the asset |
| Owner/Department | Department responsible for the asset |
| Risk Level | Low / Medium / High / Critical |
| Security Status | Secure / Warning / Vulnerable |

## How to Run

```bash
cd src
python3 asset_inventory.py
```

Requires Python 3.6+. No external dependencies — uses only the standard library (`json`, `os`).

## Repository Structure

```
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset_inventory.py       # Main application
│
├── data/
│   └── assets.json              # Persisted asset data (auto-created/updated)
│
├── tests/
│   └── test_cases.md            # Manual test cases
│
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
│
└── README.md
```

## Sample Run

Using the sample input (3 assets: A101, A102, A103), the "Display All Assets" option produces:

```
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
Asset ID        : A101
Asset Name      : HR-PC-01
Asset Type      : Workstation
IP Address      : 192.168.1.10
OS              : Windows 11
Department      : HR
Risk Level      : Medium
Status          : Secure
-----------------------------------------
Asset ID        : A102
Asset Name      : Web-Server
Asset Type      : Server
IP Address      : 192.168.1.20
OS              : Ubuntu
Department      : IT
Risk Level      : Critical
Status          : Vulnerable
-----------------------------------------
Asset ID        : A103
Asset Name      : Core-Router
Asset Type      : Router
IP Address      : 192.168.1.1
OS              : Cisco IOS
Department      : Network
Risk Level      : High
Status          : Warning
=========================================
Total Assets : 3
Critical Assets : 1
High Risk Assets : 1
Medium Risk Assets : 1
Vulnerable Assets : 1
=========================================
```

This matches the expected output in the assignment brief.

## Screenshots

The `screenshots/` folder should contain evidence of each feature running (take these yourself from your terminal after running the program):

1. `01-add-asset.png` — adding an asset
2. `02-display-assets.png` — the full inventory + summary report
3. `03-search-asset.png` — searching for an asset by ID
4. `04-update-asset.png` — updating an asset's fields
5. `05-delete-asset.png` — deleting an asset with confirmation
6. `06-security-summary.png` — close-up of the summary counts
7. `07-input-validation.png` — an invalid entry being rejected and re-prompted (e.g., wrong Asset Type or empty field)

## Notes / Design Choices

- Data is stored as a JSON list of asset objects for readability and easy inspection/editing outside the program.
- All classification fields (type, risk, status) use case-insensitive matching but store the canonical capitalized form.
- The "Add Multiple Assets" menu option was included specifically to mirror the assignment's sample input format ("Enter number of assets: 3").
