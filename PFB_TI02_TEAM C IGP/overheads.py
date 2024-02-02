

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
    
