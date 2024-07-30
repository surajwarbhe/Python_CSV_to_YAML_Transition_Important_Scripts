import csv

def process_csv(input_file, unique_file, duplicate_file):
    seen = set()
    unique_entries = []
    duplicate_entries = []
    
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        for row in csvreader:
            if all(field == '' for field in row):
                # Ignore rows that consist entirely of empty fields
                continue
            
            second_param = row[3]  # Second parameter based on your example
            if second_param in seen:
                duplicate_entries.append(row)
            else:
                seen.add(second_param)
                unique_entries.append(row)

    with open(unique_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(unique_entries)
    
    with open(duplicate_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(duplicate_entries)

# Example usage
input_file = 'C:/Users/943492/Desktop/Loki_DEV_Pipeline/Testfile2/Day1/USM_CSV_YAML/input3.csv'
unique_file = 'unique_entries.csv'
duplicate_file = 'duplicate_entries.csv'

process_csv(input_file, unique_file, duplicate_file)
