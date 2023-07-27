# Import the csv module 
import csv

# Function to read a CSV file and return the data as a list of lists
def read_csv_file(file_path):
    """
    Read a CSV file and return the data as a list of lists.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of lists containing the data from the CSV file.
    """
    # Create an empty list to store the data
    data = []

    # Open the CSV file in read mode with UTF-8 encoding and ignore BOM
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as csv_file:
        # Create a csv_reader object to read the file
        csv_reader = csv.reader(csv_file)

        # Read the headers (first row) from the CSV file and store them in the headers variable
        headers = next(csv_reader)

        # Iterate through the remaining rows in the CSV file
        for row in csv_reader:
            # Append each row to the data list
            data.append(row)

    # Return the list of lists containing the data
    return data

# Function to find the highest overhead percentage
def find_highest_overhead_percentage(overheads_file):
    """
    Find the highest overhead percentage from the data in the CSV file.

    Parameters:
        overheads_file (str): The path to the CSV file containing overhead data.

    Returns:
        str: A formatted string describing the highest overhead percentage and category.
    """
    # Read the CSV file and store the data in the overheads list of lists
    overheads = read_csv_file(overheads_file)

    # Initialize variables to store the highest overhead percentage and category
    highest_overhead_percentage = 0
    highest_overhead_category = ''

    # Iterate through each row in the overheads list
    for row in overheads:
        try:
            # Convert the percentage value in the second column to a float
            overhead_percentage = float(row[1])

            # Check if the current overhead percentage is higher than the highest recorded so far
            if overhead_percentage > highest_overhead_percentage:
                # Update the highest overhead percentage and category if needed
                highest_overhead_percentage = overhead_percentage
                highest_overhead_category = row[0]
        except ValueError:
            # Handle any potential conversion errors for the percentage values
            print(f"Error converting percentage value: {row[1]}")

    # Create a formatted string with the highest overhead percentage and category
    overhead_output = "[HIGHEST OVERHEAD] {}: {:.2f}%".format(highest_overhead_category, highest_overhead_percentage)

    # Return the final output string
    return overhead_output

