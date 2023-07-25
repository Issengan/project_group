from overheads import find_highest_overhead_percentage
from cash_on_hand import display_cash_scenarios
from profit_loss import display_profit_loss_scenarios 

def main():
    # Find highest overhead percentage
    overheads_file = "C:/project_group/csv_reports/Overheads.csv"
    highest_overhead_output = find_highest_overhead_percentage(overheads_file)

    # Display cash scenarios
    cash_on_hand_file = "C:/project_group/csv_reports/Cash_on_Hand.csv"
    cash_output = display_cash_scenarios(cash_on_hand_file)

    # Display profit and loss scenarios
    profit_loss_file = "C:/project_group/csv_reports/Profits_and_Loss.csv"
    profit_loss_output = display_profit_loss_scenarios(profit_loss_file)

    # Write the outputs to the summary_report.txt file
    with open("summary_report.txt", "w") as file:
        file.write(highest_overhead_output + "\n")
        file.write(cash_output)
        file.write(profit_loss_output)

if __name__ == "__main__":
    main()
