import csv
import os

def save_lead(intent, name, location, phone, email, budget=None, postcode=None, home_type=None):
    file_path = "leads.csv"
    fieldnames = ["intent", "name", "location", "phone", "email", "budget", "postcode", "home_type"]

    # Check if file exists
    file_exists = os.path.isfile(file_path)

    # Open file in append mode
    with open(file_path, mode="a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if file is newly created
        if not file_exists:
            writer.writeheader()

        # Write lead data
        writer.writerow({
            "intent": intent,
            "name": name,
            "location": location,
            "phone": phone,
            "email": email,
            "budget": budget or "",
            "postcode": postcode or "",
            "home_type": home_type or ""
        })
