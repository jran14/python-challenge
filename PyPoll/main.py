import os
import csv 
import statistics
import pandas as pd
import sys
#append to results to empty lists 
Khan= 'Khan' 
Total_Khan= []
C= []
L= []
O= []

#read the csv
csvpath=os.path.join('..','Data','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #to count the total number of votes
    data=list(csvreader)
    row_count= len(data)

# print the heading
print('ELECTION RESULTS')
print('--------------------------------------')

# total votes
print('TOTAL VOTES:', row_count) 

print('--------------------------------------')

# 4 candidates, percentages, number of votes
#panda dataframe
df= pd.read_csv(csvpath)

#group by Candidate
df1= df.groupby('Candidate').count()

#find the percentage of total votes for each candidate
df2= df1.rename(columns={"Voter ID": "TOTAL VOTES", "County": "PERCENTAGE"})
df2['PERCENTAGE']=(df2['TOTAL VOTES'] / int(row_count)).astype(float).map("{:.2%}".format)
print(df2)

print('--------------------------------------')
#print winner
print('WINNER IS ', df2['TOTAL VOTES'].idxmax())

print('--------------------------------------')

#print results to txt 
stdoutOrigin=sys.stdout 
sys.stdout = open("PyPollResults.txt", "w")
print('ELECTION RESULTS')
print('--------------------------------------')
print('TOTAL VOTES:', row_count) 
print('--------------------------------------')
print(df2)
print('--------------------------------------')
print('WINNER IS ', df2['TOTAL VOTES'].idxmax())
print('--------------------------------------')
sys.stdout.close()
sys.stdout=stdoutOrigin