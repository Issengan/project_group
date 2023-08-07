# Import necessary functions from respective modules
from overheads import find_highest_overhead_percentage
from cash_on_hand import display_cash_scenarios
from profit_loss import display_profit_loss_scenarios

def main():
    """
    Main function to execute the analysis and generate the summary report.
    1. Find highest overhead percentage from the 'Overheads.csv' file.
    2. Display cash scenarios using data from 'Cash_on_Hand.csv' file.
    3. Display profit and loss scenarios using data from 'Profits_and_Loss.csv' file.
    4. Write the outputs of all scenarios to the 'summary_report.txt' file.
    """
    # Find highest overhead percentage
    overheads_file = "../project_group/csv_reports/Overheads.csv"
    highest_overhead_output = find_highest_overhead_percentage(overheads_file)

    # Display cash scenarios
    cash_on_hand_file = "../project_group/csv_reports/Cash_on_Hand.csv"
    cash_output = display_cash_scenarios(cash_on_hand_file)

    # Display profit and loss scenarios
    profit_loss_file = "../project_group/csv_reports/Profits_and_Loss.csv"
    profit_loss_output = display_profit_loss_scenarios(profit_loss_file)

    with open("summary_report.txt", "w") as file:
        file.write(highest_overhead_output + "\n")
        file.write(cash_output)
        file.write(profit_loss_output)

    # The following block of code will only be executed if this script is run as the main program.
    # This condition checks whether the script is being run directly and not imported as a module.
    # Call the main function to execute the analysis and generate the summary report.
    if __name__ == "__main__":
        main()

