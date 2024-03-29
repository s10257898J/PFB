from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    overheads=[] 

    # Append overhead records into the overheads list.
    for row in reader:
        # Get the category and overhead value for each record and append to the overheads list.
        overheads.append({
            'category': row[0],
            'overheads': float(row[1])
        })

# Initialize variables to keep track of the maximum overhead and its corresponding category
max_overhead_category = ""
max_overhead_value = 0.0

# Iterate through the list of overheads
for entry in overheads:
    if entry['overheads'] > max_overhead_value:
        max_overhead_value = entry['overheads']
        max_overhead_category = entry['category']

print(f"[HIGHEST OVERHEAD] {max_overhead_category}: {max_overhead_value}%")

# Write the result to a text file.
with open("(Overheads)summary_report.txt", "w") as overhead_textfile:
    overhead_textfile.write(f"[HIGHEST OVERHEAD] {max_overhead_category}: {max_overhead_value}%")
    
