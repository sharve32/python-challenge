import os
import csv

#path to collect data from csv
csvpath = os.path.join("Resources/budget_data.csv")

with open(csvpath, newline="") as csvfile:
    data_reader = csv.reader(csvfile, delimiter=',')
    header = next(data_reader)
    bank_list = []
    last_month = 0
    months = 0
    total = 0
    for row in data_reader:
        bank_list.append(row)
        if months == 0:
            bank_list.append(row)
        elif months > 0:
            bank_list[months].append(int(bank_list[months][1]) - last_month)
        last_month = int(bank_list[months][1])
        total += int(row[1])
        months += 1
    total_change = 0.0
    profit_loss = []   
    for counter in range(0, (months)):
        profit_loss.append(int(bank_list[counter][2]))
        total_change += int(profit_loss[counter])

max_profit_in = profit_loss.index(max(profit_loss))
max_loss_in = profit_loss.index(min(profit_loss))

#Format values to currency
max_profit = '${:,.2f}'.format(max(profit_loss))
max_loss = '${:,.2f}'.format(min(profit_loss))
avg_change = '${:,.2f}'.format(total_change/(months-1))
total= '${:,.2f}'.format(total)

#Print to terminal
print("Financial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {months}\n")
print(f"Total Net: {total}\n")
print(f"Average Change: {avg_change}\n")
print(f"Greatest Increase in Profits: {bank_list[max_profit_in][0]} ({max_profit})\n")
print(f"Greatest Decrease in Profits: {bank_list[max_loss_in][0]} ({max_loss})\n")

#Set up and open external text file to write
output = open("Resources/analyzed_budget.txt", 'w+')

#Write to external text file
output.write("Financial Analysis\n")
output.write("----------------------------\n")
output.write("Total Months: {months}\n")
output.write("Total Net: {total}\n")
output.write("Average Change: {avg_change}\n")
output.write("Greatest Increase in Profits: {bank_list[max_profit_in][0]} ({max_profit})\n")
output.write("Greatest Decrease in Profits: {bank_list[max_loss_in][0]} ({max_loss})\n")

#Close relevant external files
output.close()
csvfile.close()

