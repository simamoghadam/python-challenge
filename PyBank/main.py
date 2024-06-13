import os
import csv

# Initialize variables
total_months = 0
total_profit_losses = 0
changes = []
previous_profit = 0
# Initialize dictionaries to store the greatest increase and decrease
greatest_increase = {"date": "", "amount": float("-inf")}  
greatest_decrease = {"date": "", "amount": float("inf")}  

# Path to the CSV file
pybank_csv = os.path.join("C:\\Users\\61433\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv")

# Open the CSV file
with open(pybank_csv, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)  # Skip the header row

    # Loop through each row in the CSV file
    for row in csv_reader:
        current_profit = int(row[1])

        # Count total months and calculate total profit/losses
        total_months += 1
        total_profit_losses += current_profit

        # Calculate profit/loss change and store it in a list
        if previous_profit !=0 :
            change = current_profit - previous_profit
            changes.append(change)
            
            # Update greatest increase if the current change is greater
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = row[0]

            # Update greatest decrease if the current change is smaller
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = row[0]

        previous_profit = current_profit

    # Calculate the average change
    average_change = sum(changes) / len(changes)

    # Print the results
    print(f"Total Months: {total_months}")
    print(f"Total Profit/Losses: {total_profit_losses}")
    print(f"Average Change: {average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Path to the output text file
output_path = os.path.join("C:\\Users\\61433\\Desktop\\python-challenge\\PyBank\\analysis\\financial_analysis.txt")

# Prepare the results
results = [
    "Financial Analysis\n",
    "----------------------------\n\n",
    f"Total Months: {total_months}\n\n",

    f"Total Profit/Losses: ${total_profit_losses}\n\n",

    f"Average Change: ${average_change:.2f}\n\n",

    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n\n",

    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
]

# Write the results to the text file
with open(output_path, "w") as txt_file:
    txt_file.writelines(results)
