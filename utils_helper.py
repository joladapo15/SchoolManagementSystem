import csv

def save_to_csv(filename, data, fieldnames):
    """Save a list of dictionaries to a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)



