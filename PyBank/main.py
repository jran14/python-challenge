import os
import csv 
import statistics
pl = []
delta = []
#to read the csv file
csvpath=os.path.join('..','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    months = 0
    for row in csvreader:
        x = int(row[1])
        pl.append(x)
        months= months + 1
      #  print(pl)
        



#print(pl)
#printing financial Analysis heading
print('FINANCIAL ANALYSIS')
print('----------------------------------')
#Total Months
print('Total Number of Months', months)
#total profit/loss
print('Total Profit:',sum(pl))

#average change in P/L over time
for i in range(months-1):
    delta.append(pl[i+1]-pl[i])
print('Average Change:', statistics.mean(delta))
#print('Average Change:', '10.2f' % statistics.mean(delta))
#greatest increase in profits
print('Greatest Increase:', max(delta))
#greatest decrease in losses 
print('Greatest Decrease:', min(delta))

