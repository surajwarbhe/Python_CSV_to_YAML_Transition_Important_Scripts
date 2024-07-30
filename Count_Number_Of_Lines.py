import csv

def count_lines_in_csv(csv_file):
    line_count = 0
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            line_count += 1
    return line_count

if __name__ == "__main__":
    # Specify the full path to your input CSV file
    input_csv = 'C:/Users/943492/Desktop/Loki_DEV_Pipeline/Testfile2/Day1/USM_CSV_YAML/main_USM.csv'
    
    num_lines = count_lines_in_csv(input_csv)
    print(f"The number of lines in the CSV file is: {num_lines}")
