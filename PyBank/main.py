import os
import csv 
import statistics
import sys
pl = []
delta = []
mon=[]
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
        mon.append(row[0])
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
m = statistics.mean(delta)
print('Average Change: ${:.2f}'.format(m))
#print('Average Change:', '$', round(statistics.mean(delta)))
#print('Average Change:', '10.2f' % statistics.mean(delta))

#greatest increase in profits
#for rows in csvreader:
   # if delta == max(delta)
   # print(row[0])
max1= delta.index(max(delta))
#print(max1)
print('Greatest Increase in Profits:', mon[max1+1], '(',max(delta),')')
#greatest decrease in losses 
min1=delta.index(min(delta))
#print(min1)
print('Greatest Decrease in Profits:',  mon[min1+1], '(',min(delta),')')

#print to txt file

stdoutOrigin=sys.stdout 
sys.stdout = open("PyBankResults.txt", "w")
print('FINANCIAL ANALYSIS')
print('----------------------------------')
print('Total Number of Months', months)
print('Total Profit:',sum(pl))
print('Average Change: ${:.2f}'.format(m))
print('Greatest Increase in Profits:', mon[max1+1], '(',max(delta),')')
print('Greatest Decrease in Profits:',  mon[min1+1], '(',min(delta),')')

sys.stdout.close()
sys.stdout=stdoutOrigin