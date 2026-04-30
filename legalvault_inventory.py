import csv
from pathlib import Path

BASE_FOLDER = Path("Sampledocuments")
OUTPUT_FILE = "legalvault_inventory.csv"

DOCUMENT_RULES = {
    "Casenotes": {
        "document_type": "Case Note",
        "sensitivity": "Highly Confidential",
        "suggested_access": "Attorney, Paralegal"
    },
    "Clientletters": {
        "document_type": "Client Letter",
        "sensitivity": "Confidential",
        "suggested_access": "Attorney, Paralegal"
    },
    "Intake": {
        "document_type": "Client Intake Form",
        "sensitivity": "Confidential",
        "suggested_access": "Attorney, Paralegal, Receptionist"
    },
    "Policies": {
        "document_type": "Office Policy",
        "sensitivity": "Internal",
        "suggested_access": "Attorney, Paralegal, Receptionist"
    }
}

def classify_document(file_path):
    folder_name = file_path.parent.name

    rule = DOCUMENT_RULES.get(folder_name, {
        "document_type": "Unknown",
        "sensitivity": "Review Required",
        "suggested_access": "Attorney Review Required"
    })

    return {
        "file_name": file_path.name,
        "folder": folder_name,
        "document_type": rule["document_type"],
        "sensitivity": rule["sensitivity"],
        "suggested_access": rule["suggested_access"]
    }

def main():
    if not BASE_FOLDER.exists():
        print(f"Error: {BASE_FOLDER} folder was not found.")
        return

    files = list(BASE_FOLDER.rglob("*.txt"))

    if not files:
        print("No legal document files found.")
        return

    with open(OUTPUT_FILE, "w", newline="") as csvfile:
        fieldnames = [
            "file_name",
            "folder",
            "document_type",
            "sensitivity",
            "suggested_access"
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for file_path in files:
            document_record = classify_document(file_path)
            writer.writerow(document_record)

    print(f"Inventory created successfully: {OUTPUT_FILE}")
    print(f"Total documents scanned: {len(files)}")

if __name__ == "__main__":
    main()