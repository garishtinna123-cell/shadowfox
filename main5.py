import csv

records = []

# Read data from CSV file
with open("employeescores.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        score1 = int(row["Score1"])
        score2 = int(row["Score2"])
        score3 = int(row["Score3"])

        total_score = score1 + score2 + score3
        average_score = total_score / 3

        result = "Pass" if average_score >= 50 else "Fail"

        row["Total_Score"] = total_score
        row["Average_Score"] = round(average_score, 2)
        row["Result"] = result

        records.append(row)

# Write updated data to a new CSV file
if records:
    with open("employeescores_updated.csv", "w", newline="") as new_file:
        fieldnames = records[0].keys()
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(records)

    print("Updated CSV file created successfully.")
else:
    print("No records found.")
