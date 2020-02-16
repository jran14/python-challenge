import os
import csv 
import statistics
import sys
#append results to empy lists
pl = []
delta = []
mon=[]
#to read the csv file
csvpath=os.path.join('..','Data','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    months = 0
    #list revenue and count months
    for row in csvreader:
        x = int(row[1])
        pl.append(x)
        mon.append(row[0])
        months= months + 1

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
#print result rounded to two decimal places
print('Average Change: ${:.2f}'.format(m))

#find the greatst increase in profits
max1= delta.index(max(delta))
print('Greatest Increase in Profits:', mon[max1+1], '(',max(delta),')')

#find the greatest decrease in losses 
min1=delta.index(min(delta))
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