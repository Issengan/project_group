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
