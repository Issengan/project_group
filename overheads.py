import csv

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Read the header row
        for row in csv_reader:
            data.append(row)
    return data

def find_highest_overhead_percentage(overheads_file):
    overheads = read_csv_file(overheads_file)
    highest_overhead_percentage = 0
    highest_overhead_category = ''

    for row in overheads:
        try:
            overhead_percentage = float(row[1])
            if overhead_percentage > highest_overhead_percentage:
                highest_overhead_percentage = overhead_percentage
                highest_overhead_category = row[0]
        except ValueError:
            # Handle any potential conversion errors for the percentage values
            print(f"Error converting percentage value: {row[1]}")

    overhead_output = "[HIGHEST OVERHEAD] {}: {:.2f}%".format(highest_overhead_category, highest_overhead_percentage)
    return overhead_output
