# import os module for navigating through operating systems
import os
# import csv module to read csv files
import csv

# create a path to csv file
csvpath =os.path.join(".","Resources","budget_data.csv")

#Create empty lists to iterate through the specified rows for the following variables
total_months= []
total_profit=[]
monthly_profit_change=[]

# Open and read the csv file 
with open(csvpath,"r") as csvfile:
    
    #Use csv reader to seperate variables by delimiter and store contents
    csvreader=csv.reader(csvfile,delimiter=",")

    #skip header to iterate with the values
    header=next(csvreader)

    #read and iterate through the rows in reader
    for row in csvreader: 
        #append the total months and total profit to their respective lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #iterate through profits to get monthly change in profits
    for i in range(len(total_profit)-1):

        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# calculate the max and min of the new monthly profit change list 
max_increase_value = max(monthly_profit_change)
min_decrease_value = min(monthly_profit_change)
max_decrease_value= max(monthly_profit_change)

# Correlate max and min to the proper month using the month list and index from max and min
#Use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 


# Print Statements
print(f"Financial Summary")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${max_increase_value})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${max_decrease_value})")
# Assign output file location 
financial_summary =os.path.join(".","Analysis","financial_summary.txt")

with open(financial_summary,"w") as file:

# Write methods to print to Financial_Analysis_Summary 
    file.write(f"Financial Summary")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")



