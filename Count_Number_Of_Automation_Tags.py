import yaml

def count_automation_tags(yaml_file):
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    count = 0

    def count_tags(obj):
        nonlocal count
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == 'AutomationTags':
                    count += 1
                count_tags(value)
        elif isinstance(obj, list):
            for item in obj:
                count_tags(item)
    
    count_tags(data)
    return count

if __name__ == "__main__":
    yaml_file = 'C:/Users/943492/Desktop/Loki_DEV_Pipeline/Testfile2/Day1/USM_CSV_YAML/output2.yaml'
    
    count = count_automation_tags(yaml_file)
    print(f"The number of '- AutomationTags:' in the YAML file is: {count}")
