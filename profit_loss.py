import csv 

def read_csv_file(file_path): 
    data = [] 
     
    with open(file_path, 'r') as csv_file: 
        csv_reader = csv.reader(csv_file) 
        headers = next(csv_reader) 

        for row in csv_reader: 
            data.append(dict(zip(headers, row))) 
          
    return data 

def display_profit_loss_scenarios(profit_loss_file): 
    profit_loss_data = read_csv_file(profit_loss_file) 
 
    output = "" 
    positive_net_profit = all(float(row['Net Profit']) >= 0 for row in profit_loss_data) 
  
    if positive_net_profit: 
        output += "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n" 
        highest_surplus_day = None 
        highest_surplus_amount = 0 
      
        for i in range(1, len(profit_loss_data)): 
            current_net_profit = float(profit_loss_data[i]['Net Profit']) 
            previous_net_profit = float(profit_loss_data[i - 1]['Net Profit']) 
   
            if current_net_profit > previous_net_profit: 
                net_profit_surplus = current_net_profit - previous_net_profit 
   
            if net_profit_surplus > highest_surplus_amount: 
                    highest_surplus_day = i 
                    highest_surplus_amount = net_profit_surplus 
              
        if highest_surplus_day is not None: 
            output += "[HIGHEST NET PROFIT SURPLUS] DAY: {}, AMOUNT: USD{}\n".format(highest_surplus_day, int(highest_surplus_amount)) 
    else: 
        
        for i in range(1, len(profit_loss_data) - 1): 
            current_net_profit = float(profit_loss_data[i]['Net Profit']) 
            previous_net_profit = float(profit_loss_data[i - 1]['Net Profit']) 
 
             
            if current_net_profit < previous_net_profit: 
                net_profit_deficit = previous_net_profit - current_net_profit
              
                output += "[PROFIT DEFICIT] DAY: {}, AMOUNT: USD{}\n".format(i + 1, int(net_profit_deficit)) 
              
    return output
