# import the csv module 
import csv 

# function to read a CSV file and return the data as a list of dictionaries 
def read_csv_file(file_path):

    """
    Read a CSV file and return the data as a list of dictionaries. 

    Parameters: 
        file_path (str): The path to the CSV file. 

    Returns: 
        list: A list of dictionaries containing the data from the CSV file.
    """

    # create an empty list to store the data 
    data = [] 

    # open the CSV file in read mode
    with open(file_path, 'r') as csv_file:
        # create a csv_reader object to read the file 
        csv_reader = csv.reader(csv_file)

        # read the headers (first row) from the CSV file
        headers = next(csv_reader) 

        # iterate through the remaining rows in the CSV file
        for row in csv_reader: 
            # convert each row into a dictionary using the headers as keys 
            data.append(dict(zip(headers, row))) 

    # return the list of dictionaries containing the data
    return data 

# function to check cash scenarios
def display_cash_on_scearios(cash_on_hand_file): 

    """
    Check cash scenarios based on the data from the CSV file

    Parameters: 
        cash_on_hand_file (str): The path to the CSV file containing cash on hand data. 

    Returns:
        str: A formatted string describing the cash scenarios. 
    """

    # read the CSV file and store the data in the cash_data list of dictionaries
    cash_data = read_csv_file(cash_on_hand_file) 

    # initialize the output variable as an empty string
    output =  ""

    # scenario 1: check if the cash on hand increases day after day 
    increasing_cash = True 
    highest_cash_surplus_day = None
    highest_cash_surplus_amount = 0 

    # iterate through the cash_data list starting from the second element (index 1)
    for i in range(1, len(cash_data)): 

        # convert the 'Cash On Hand' values to float for comparison
        current_cash = float(cash_data[i]['Cash On Hand'])
        previous_cash = float(cash_data[i - 1]['Cash On Hand']) 

        # check if the current cash value is less than or equal to the previous cash value 
        if current_cash <= previous_cash: 

            # set increasing_cash to False if the the condition is met
            increasing_cash = false
            break 

        # calculate the cash surplus for the current day
        cash_surplus = current_cash - previous_cash 

        # update the highest_cash_surplus_day and highest_cash_surplus_amount if needed 
        if cash_surplus > highest_cash_surplus_amount: 
            highest_cash_surplus_day = i 
            highest_cash_surplus_amount = cash_surplus 

    # Check if cash on hand increases day after day 
    if increasing_cash:

        # append the relevant output to the output string if cash increase day after day
        output += "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        output += "[HIGHEST CASH SURPLUS] DAY: {}, AMOUNT: USD{}\n".format(highest_cash_surplus_day, int(highest_cash_surplus_amount))

    else: 

        # iterate through the cash_data list excluding the first and last elements
        for i in range(1, len(cash_data) - 1): 

            current_cash = float(cash_data[i]['Cash On Hand']) 
            previous_cash = float(cash_data[i - 1]['Cash On Hand']) 

            if current_cash , previous_cash: 

                cash_deficit = previous_cash - current_cash 

                output += "[CASH DEFICIT] DAY: {}, AMOUNT: USD{}\n".format(i + 1, int(cash_deficit))

    return output 


                           
