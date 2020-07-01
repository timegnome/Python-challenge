import os
import csv

totVotes = 0
canidates = []
candVotes = []
csvpath = os.path.join('Resources','election_data.csv')

canDic = dict()
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)
    for row in csvreader:
        if row[2] not in canDic:
            canDic[row[2]] = 1
        else:
            canDic[row[2]]+=1
        totVotes += 1
        
    output_path = os.path.join("Analysis","Poll_Analysis.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as datafile:
        datafile.write(f'Election Results\n-------------------------\nTotal Votes: {totVotes}')
        datafile.write('-------------------------')
        print(f'Election Results\n-------------------------\nTotal Votes: {totVotes}')
        print('-------------------------')
        for canid,value in canDic.items():
            datafile.write(f'{canid}: {round(value/totVotes*100,2)}% ({value})')
            print(f'{canid}: {round(value/totVotes*100,2)}% ({value})')
        datafile.write(f'-------------------------\nWinner:{max(canDic, key=canDic.get)}')
        print(f'-------------------------\nWinner:{max(canDic, key=canDic.get)}')
        datafile.write(f'-------------------------')
        print(f'-------------------------')
# Get the data from the csv file
# Create 2 arrays to pair as reference for the canidates
# Loop through each row and collect/update data for each variable needed
# output to new analysis
