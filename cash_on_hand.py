import csv 

def read_csv_file(file_path):

    data = [] 

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        headers = next(csv_reader) 

        for row in csv_reader: 
            data.append(dict(zip(headers, row))) 
          
    return data 

def display_cash_on_scearios(cash_on_hand_file): 

    cash_data = read_csv_file(cash_on_hand_file) 

    output =  ""

    increasing_cash = True 
    highest_cash_surplus_day = None
    highest_cash_surplus_amount = 0 

    for i in range(1, len(cash_data)): 

        current_cash = float(cash_data[i]['Cash On Hand'])
        previous_cash = float(cash_data[i - 1]['Cash On Hand']) 

        if current_cash <= previous_cash: 

            increasing_cash = false
            break 

        cash_surplus = current_cash - previous_cash 

        if cash_surplus > highest_cash_surplus_amount: 
            highest_cash_surplus_day = i 
            highest_cash_surplus_amount = cash_surplus 


                           
