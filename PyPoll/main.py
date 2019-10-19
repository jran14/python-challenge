import os
import csv 
import statistics
import pandas as pd
import sys

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
#Vote_count= df['Candidate'].value_counts()

#Pct= df['Candidate'].value_counts() / row_count

#print(df['Candidate'].value_counts(), '{:.2%}'.format(pct))



#group by Candidate
df1= df.groupby('Candidate').count()

#print(df1)
df2= df1.rename(columns={"Voter ID": "TOTAL VOTES", "County": "PERCENTAGE"})
df2['PERCENTAGE']=(df2['TOTAL VOTES'] / int(row_count)).astype(float).map("{:.2%}".format)
print(df2)

#print(can.first())
print('--------------------------------------')
# winner 
#df_series= pd.to_numeric(df2)
#df2['TOTAL VOTES']= pd.to_numeric(df2['TOTAL VOTES'])

#elec_winner= df2['TOTAL VOTES'].max()
#print(df2.loc([0,df2.values.argmax()])
#print(df2.at[2,'TOTAL VOTES'])
#print(df.loc[df['Voter Id'].idxmax()], 'Candidate')
#print(df2)
print('WINNER IS ', df2['TOTAL VOTES'].idxmax())
#print(df2.loc[0,int(elec_winner)])

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