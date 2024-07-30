import json
import yaml

# Read the JSON file
with open('new_USM_ONESTOR_V5_GF_Manifest.json', 'r') as json_file:
    # Parse the JSON data
    json_data = json_file.read()

# Convert JSON data to Python objects
python_objects = json.loads(json_data)

# Write Python objects to YAML file
with open('USM_ONESTOR_V5_GF_Manifest1.yaml', 'w') as yaml_file:
    # Convert Python objects to YAML and write to file
    yaml.dump(python_objects, yaml_file, default_flow_style=False)

print("Conversion successful!")
