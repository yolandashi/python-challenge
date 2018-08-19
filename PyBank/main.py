import os
import csv

csvpath = os.path.join('budget_data.csv')


total_months = 0
total_net_amount = 0
average_change=0
previous_month_profit=0
profit_change=[]
greatest_increase = [0,0]
greatest_decrease = [0,0]


with open(csvpath, newline='',encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        total_months = total_months + 1
        total_net_amount = total_net_amount + int(row[1])
        monthly_profit_change=int(row[1])-int(previous_month_profit)
        profit_change.append(monthly_profit_change)
        average_change = round(sum(profit_change)/len(profit_change), 2)
    

        greatest_increase = max(profit_change)
        greatest_decrease = min(profit_change)


cleaned_csv =(
            f"Financial Analysis\n"
            f"----------------------------\n"
            f"Total Months: + {total_months}\n"
            f"Total Net Amount: $ + {total_net_amount}\n"
            f"Average Change: $ + {average_change}\n"
            f"Greatest Increase: $ + {greatest_increase}\n"
            f"Greatest Decrease: $ + {greatest_decrease}\n")
print(cleaned_csv)


output_file = os.path.join("output.csv")
with open(output_file, "w", newline="", encoding="utf-8") as datafile:
   writer = csv.writer(datafile)
   writer.writerow([cleaned_csv])
    
    


    