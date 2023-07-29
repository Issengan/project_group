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
 

  
