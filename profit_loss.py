#Import the csv module
import csv
#Function to read CSV file and return data as a list of dictionaries
def read_csv_file(file_path):
  """
  Read a CSV file and return the data as a list of dictionaries.
  Parameters: 
        file_path (str): The path to the CSV file. 
 
    Returns: 
        list: A list of dictionaries containing the data from the CSV file. 
    """ 

   # Create an empty list to store the data 
    data = [] 
 
    # Open the CSV file in read mode 
    with open(file_path, 'r') as csv_file: 
        # Create a csv_reader object to read the file 
        csv_reader = csv.reader(csv_file) 
 
  # Read the headers (first row) from the CSV file and store them in the headers variable 
        headers = next(csv_reader) 
 
        # Iterate through the remaining rows in the CSV file 
        for row in csv_reader: 
            # Convert each row into a dictionary using the headers as keys 
            data.append(dict(zip(headers, row))) 
 
    # Return the list of dictionaries containing the data 
    return data 

  
