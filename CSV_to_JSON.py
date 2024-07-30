import csv
import json

CSV_FILENAME = "USM_ONESTOR_V5_GF_Manifest.csv"
JSON_FILENAME = "new_USM_ONESTOR_V5_GF_Manifest.json"

def create_json_for_parent_and_subcomponents(parent, subcomponents):
    entry = {
        "parent": parent,
        "subcomponents": subcomponents
    }
    return entry

entries = []
last_parent = None
subcomponents = []

with open(CSV_FILENAME, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line_parts in csv_reader:
        if not line_parts or line_parts[0].strip() == '':
            continue  # Skip empty lines
        line_start = line_parts[0].strip()
        if line_start == '-':
            # Flush the current parent and its subcomponents if any
            if last_parent:
                entries.append(create_json_for_parent_and_subcomponents(last_parent, subcomponents))
                subcomponents = []
            last_parent = line_parts[1].strip() if len(line_parts) > 1 else None
        elif line_start == '*':
            if last_parent:
                subcomponent = line_parts[1].strip() if len(line_parts) > 1 else ''
                subcomponents.append(subcomponent)

# Ensure the last parent and its subcomponents are written
if last_parent:
    entries.append(create_json_for_parent_and_subcomponents(last_parent, subcomponents))

# Write all entries to the JSON file
with open(JSON_FILENAME, 'w') as json_file:
    json.dump(entries, json_file, indent=4)

print("JSON conversion completed.")
