import yaml
from collections import defaultdict

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def check_unique_filenames(image_files):
    filename_dict = defaultdict(list)
    for entry in image_files:
        if not isinstance(entry, dict):
            print(f"Unexpected entry format: {entry}")
            continue
        
        filename = entry.get('filename')
        if filename:
            filename_dict[filename].append(entry)
        else:
            print(f"Entry missing 'filename': {entry}")
    
    unique_entries = []
    duplicate_entries = []
    
    for filename, entries in filename_dict.items():
        if len(entries) == 1:
            unique_entries.extend(entries)
        else:
            duplicate_entries.extend(entries)
    
    return unique_entries, duplicate_entries

def main():
    input_file = 'C:/Users/943492/Desktop/Loki_DEV_Pipeline/Testfile2/Day1/USM_CSV_YAML/input.yaml'
    unique_output_file = 'unique_filenames2.yaml'
    duplicate_output_file = 'duplicate_filenames2.yaml'
    
    data = read_yaml(input_file)
    
    if 'ManifestItems' not in data or 'ImageFiles' not in data['ManifestItems']:
        print("Input YAML file does not contain 'ManifestItems' or 'ImageFiles'.")
        return
    
    image_files = data['ManifestItems']['ImageFiles']
    
    unique_entries, duplicate_entries = check_unique_filenames(image_files)
    
    unique_output = {'ManifestItems': {'ImageFiles': unique_entries}}
    duplicate_output = {'ManifestItems': {'ImageFiles': duplicate_entries}}
    
    write_yaml(unique_output, unique_output_file)
    write_yaml(duplicate_output, duplicate_output_file)
    
    print(f"Unique entries written to {unique_output_file}")
    print(f"Duplicate entries written to {duplicate_output_file}")

if __name__ == "__main__":
    main()


#    input_file = 'C:/Users/943492/Desktop/Loki_DEV_Pipeline/Testfile2/Day1/USM_CSV_YAML/input.yaml'

