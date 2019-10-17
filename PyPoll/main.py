import os
import csv 
import statistics
import pandas as pd

Khan= 'Khan' 
Total_Khan= []
C= []
L= []
O= []


csvpath=os.path.join('..','election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #to count the total number of votes
    data=list(csvreader)
    row_count= len(data)
    #to count the number of votes for each candidate
    #for row in csvreader:
         #if row[2] == Khan:
            #Total_Khan.append(row[2])


    #print(f"CSV Header: {csv_header}")

# print the heading
print('ELECTION RESULTS')
print('--------------------------------------')

# total votes

print('TOTAL VOTES:', row_count) 

print('--------------------------------------')
# 4 candidates, percentages, number of votes

#panda dataframe
df= pd.read_csv(csvpath)
#print(df['Candidate'].unique())
Vote_count= df['Candidate'].value_counts()
pct= df['Candidate'].value_counts() / df['Candidate'].value_counts().sum()

#Pct= df['Candidate'].value_counts() / row_count

print(df['Candidate'].value_counts(), '{:.2%}'.format(pct))



#group by Candidate
#can=df.groupby('Candidate').average()
#print(can.first())



print('--------------------------------------')
# winner 

print('--------------------------------------')