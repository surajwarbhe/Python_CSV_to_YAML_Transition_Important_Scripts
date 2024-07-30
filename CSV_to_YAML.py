import csv
import yaml

def csv_to_yaml(csv_input, yaml_output):
    with open(csv_input, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        yaml_data = []
        current_component = None
        
        for row in csv_reader:
            if row['-'] == '*':
                if current_component:
                    yaml_data.append(current_component)
                current_component = {
                    'COMPONENT_FILES': [],
                    'TARGET_FILE': row['TARGET_FILE'],
                    'TYPE': row['TYPE'],
                    'P1': row['P1'],
                    'P2': row['P2'],
                    'MEM': row['MEM'],
                    'sideplane': '',
                    'cmdlinegetter': 'non_config_type_cmd_line_getter'
                }
                for i in range(1, 8):
                    if row[f'F{i}PID'] and row[f'F{i}DID'] and row[f'F{i}NAME']:
                        current_component['COMPONENT_FILES'].append({
                            'FILE_ID': row[f'F{i}DID'],
                            'FILE_NAME': row[f'F{i}NAME'],
                            'TARGET_ID': row[f'F{i}PID']
                        })
            elif row['-'] == '-' and current_component:
                yaml_data.append(current_component)
                current_component = None

        if current_component:
            yaml_data.append(current_component)

    with open(yaml_output, 'w') as yaml_file:
        yaml.dump(yaml_data, yaml_file, sort_keys=False, default_flow_style=False)

csv_input = r'C:\Users\943492\Desktop\Loki_DEV_Pipeline\Testfile2\test.csv'
yaml_output = 'Loki_output1.yaml'
csv_to_yaml(csv_input, yaml_output)
