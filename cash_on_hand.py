import csv

# Function to read a CSV file and return the data as a list of dictionaries
def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Read the headers
        for row in csv_reader:
            data.append(dict(zip(headers, row)))
    return data

# Function to check cash scenarios
def display_cash_scenarios(cash_on_hand_file):
    cash_data = read_csv_file(cash_on_hand_file)
    output = ""  # Initialize the output variable

    # Scenario 1: Check if cash on hand increases day after day
    increasing_cash = True
    highest_cash_surplus_day = None
    highest_cash_surplus_amount = 0

    for i in range(1, len(cash_data)):
        current_cash = float(cash_data[i]['Cash On Hand'])
        previous_cash = float(cash_data[i - 1]['Cash On Hand'])

        if current_cash <= previous_cash:
            increasing_cash = False
            break

        cash_surplus = current_cash - previous_cash
        if cash_surplus > highest_cash_surplus_amount:
            highest_cash_surplus_day = i
            highest_cash_surplus_amount = cash_surplus

    if increasing_cash:
        output += "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        output += "[HIGHEST CASH SURPLUS] DAY: {}, AMOUNT: USD{}\n".format(highest_cash_surplus_day, int(highest_cash_surplus_amount))
    else:
        for i in range(1, len(cash_data) - 1):
            current_cash = float(cash_data[i]['Cash On Hand'])
            previous_cash = float(cash_data[i - 1]['Cash On Hand'])

            if current_cash < previous_cash:
                cash_deficit = previous_cash - current_cash
                output += "[CASH DEFICIT] DAY: {}, AMOUNT: USD{}\n".format(i + 1, int(cash_deficit))

    return output
