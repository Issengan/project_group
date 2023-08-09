#import the csv file
import csv 

# Function to read a CSV file and return the data as a list of dictionaries 
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

# Function to check profit and loss scenarios 
def display_profit_loss_scenarios(profit_loss_file): 
    """ 
    Check profit and loss scenarios based on the data from the CSV file. 
 
    Parameters: 
        profit_loss_file (str): The path to the CSV file containing profit and loss data. 
 
    Returns: 
        str: A formatted string describing the profit and loss scenarios. 
    """ 
    # Read the CSV file and store the data in the profit_loss_data list of dictionaries 
    profit_loss_data = read_csv_file(profit_loss_file) 
    
   # Initialize the output variable as an empty string 
    output = "" 
    
    # Scenario 1: Check if net profit is positive for all days 
    positive_net_profit = all(float(row['Net Profit']) >= 0 for row in profit_loss_data) 
    
    # Check if net profit is positive for all days 
    if positive_net_profit: 
        # Append the relevant output to the output string if net profit is positive for all days 
        output += "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n" 
        highest_surplus_day = None 
        highest_surplus_amount = 0 
        
       # Iterate through the profit_loss_data list starting from the second element (index 1) 
        for i in range(1, len(profit_loss_data)): 
            # Convert the 'Net Profit' values to float for comparison 
            current_net_profit = float(profit_loss_data[i]['Net Profit']) 
            previous_net_profit = float(profit_loss_data[i - 1]['Net Profit']) 
            
            # Check if the current net profit is higher than the previous net profit 
            if current_net_profit > previous_net_profit:
                # Calculate the net profit surplus for the current day
                net_profit_surplus = current_net_profit - previous_net_profit  
                
                # Update the highest_surplus_day and highest_surplus_amount if needed 
                if net_profit_surplus > highest_surplus_amount: 
                   highest_surplus_day = i 
                   highest_surplus_amount = net_profit_surplus 
                
        # Check if there is a highest net profit surplus and append the relevant output             
        if highest_surplus_day is not None: 
            output += "[HIGHEST NET PROFIT SURPLUS] DAY: {}, AMOUNT: USD{}\n".format(highest_surplus_day, int(highest_surplus_amount)) 
    else: 
         # Iterate through the profit_loss_data list excluding the first and last elements 
        for i in range(1, len(profit_loss_data) - 1): 
            # Convert the 'Net Profit' values to float for comparison 
            current_net_profit = float(profit_loss_data[i]['Net Profit']) 
            previous_net_profit = float(profit_loss_data[i - 1]['Net Profit']) 
 
            # Check if the current net profit is less than the previous net profit  
            if current_net_profit < previous_net_profit: 
                # Calculate the net profit deficit for the current day 
                net_profit_deficit = previous_net_profit - current_net_profit
                # Append the relevant output to the output string if net profit deficit is found 
                output += "[PROFIT DEFICIT] DAY: {}, AMOUNT: USD{}\n".format(i + 1, int(net_profit_deficit)) 

    # Return the final output string     
    return output
