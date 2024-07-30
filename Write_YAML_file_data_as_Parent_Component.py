import csv
import yaml
import os

def csv_to_yaml(csv_file, yaml_file):
    data = {}
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader, start=1):  # enumerate rows with index starting from 1
            if len(row) >= 3:  # Ensure row has at least 3 elements
                parent = row[1].strip()
                component = row[2].strip()

                if parent not in data:
                    data[parent] = []

                if component:
                    data[parent].append(component)
            else:
                print(f"Skipping malformed row at line {idx}: {row}")
    
    output = []
    for parent, components in data.items():
        output.append({
            'component': components,
            'parent': parent
        })
    
    with open(yaml_file, 'w') as f:
        yaml.safe_dump(output, f, default_flow_style=False)

if __name__ == "__main__":
    input_csv = 'C:/Users/943492/Desktop/Loki_DEV_Pipeline/Testfile2/Day1/input.csv'
    output_yaml = 'C:/Users/943492/Desktop/Loki_DEV_Pipeline/Testfile2/Day1/output3.yaml'
    
    csv_to_yaml(input_csv, output_yaml)
