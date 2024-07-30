import csv
import yaml

def csv_to_yaml(csv_file, yaml_file):
    output_data = {'ManifestItems': {'ImageFiles': []}}
    
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader, start=1):  # enumerate rows with index starting from 1
            # Ensure row has at least 12 elements
            if len(row) >= 12:
                directory = row[1].strip()
                asBuilt = row[2].strip()
                filename = row[3].strip()
                USMBuildType = row[4].strip()
                PickupLocation = row[5].strip()
                BuildTool = row[6].strip()
                Target = row[7].strip()
                CRCOffset = row[8].strip()
                AutomationTags = row[9].strip()

                output_data['ManifestItems']['ImageFiles'].append({
                    'directory': directory,
                    'filename': filename,
                    'PickupLocation': PickupLocation,
                    'Target': Target,
                    'USMBuildType': USMBuildType,
                    'AutomationTags': AutomationTags,
                    'BuildTool': BuildTool,
                    'CRC_Offset': CRCOffset,
                    'as_built': asBuilt
                })
            else:
                print(f"Skipping malformed row at line {idx}: {row}")

    with open(yaml_file, 'w') as f:
        yaml.safe_dump(output_data, f, default_flow_style=False)

if __name__ == "__main__":
    # Specify the full path to your input CSV file
    input_csv = 'C:/Users/943492/Desktop/Loki_DEV_Pipeline/Testfile2/Day1/USM_CSV_YAML/input2.csv'
    output_yaml = 'C:/Users/943492/Desktop/Loki_DEV_Pipeline/Testfile2/Day1/USM_CSV_YAML/output2.yaml'
    
    csv_to_yaml(input_csv, output_yaml)
