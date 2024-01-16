#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period



import os
import csv

# Datafile path to access the CSV
csvpath = os.path.join("C:/Users/katea/Columbia/Starter_Code/PyBank/Resources/budget_data.csv")


with open(csvpath) as csv_file:
    reader = csv.reader(csv_file, delimiter=",")    
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")


    # Create the list to store and find net amount of profit and loss
    profit_loss = []
    months = []
    

    #for loop to read through each row of data after header
    for rows in reader:
        profit_loss.append(int(rows[1]))
        months.append(rows[0])
 
    # Create the list to store and find pro_loss change
    pro_loss_change = []

    for x in range(1, len(profit_loss)):
        pro_loss_change.append((int(profit_loss[x]) - int(profit_loss[x-1])))
    
    # calculate average profitloss change
        average_pro_loss = sum(pro_loss_change) / len(pro_loss_change)
    
    # calculate total number of months
        total_months = len(months)

    # greatest increase using max function
        greatest_increase = max(pro_loss_change)

    # greatest decrease using min function
        greatest_decrease = min(pro_loss_change)
        
    # prints Financial Analysis to the terminal
    
        print("Financial Analysis")
        print(".....................")
        print(f"Total Months: {total_months}")
        print(f"Total: $ {sum(profit_loss)}")
        print (f"Average Change: ${average_pro_loss:.2f}")
        print("Greatest Increase in Profits: " + str(months[pro_loss_change.index(max(pro_loss_change))+1]) + " " + "($" + f"{greatest_increase}" ")")
        print("Greatest Decrease in Profits: " + str(months[pro_loss_change.index(min(pro_loss_change))+1]) + " " + "($" + f"{greatest_decrease}" ")")
        
 # create print out file
 

with open("C:/Users/katea/Columbia/Starter_Code/PyBank/Resources/output.txt", "w") as printoutfile: 
       
    printoutfile.write("Financial Analysis\n")
    
    printoutfile.write("---------------------------\n")
    
    printoutfile.write(f"Total Months:  {total_months}\n")
    
    printoutfile.write(f"Total: $ {sum(profit_loss)}\n")
    
    printoutfile.write(f"Average Change: ${average_pro_loss:.2f}\n")

    printoutfile.write("Greatest Increase in Profits: " + str(months[pro_loss_change.index(max(pro_loss_change))+1]) + " " + "($" + f"{greatest_increase}" ")\n")
    
    printoutfile.write("Greatest Decrease in Profits: " + str(months[pro_loss_change.index(min(pro_loss_change))+1]) + " " + "($" + f"{greatest_decrease}" ")\n")
    
     
