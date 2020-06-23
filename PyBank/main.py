import os
import csv
# Create variables for desired information
months = []
totalPr_Ls =0
greatestInc =['',0]
greatestDec =['',0]
# Create path and open csvfile for the data
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    csv_header = next(csvreader)
#     print(csv_header)
    prvRow = ['',0]
#     Loop through the csvfile rows 
    for row in csvreader:
        if not(months):
            first = row[1]
#             months = set(months)
#             months.add(date[0])
#         elif  date[0] not in months:
#       Collect the data for the files and update them each iteration
        date = csv_header[0].split('-')
        months.append(date[0])
        totalPr_Ls += int(row[1])
        percChng = int(row[1]) -  int(prvRow[1])
        prvRow = row
#         Check if the any changes to 
        if percChng> greatestInc[1]:
            greatestInc = [row[0],percChng]
        if percChng< greatestDec[1]:
            greatestDec = [row[0],percChng]
#    Create Path name to file
    output_path = os.path.join("Analysis","Bank_Analysis.txt")
    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as datafile:
#       Print to terminal and file
        datafile.write("Financial Analysis\n----------------------------")
        print("Financial Analysis\n----------------------------")
        datafile.write(f'Total Months: ${len(months)}')
        print(f'Total Months: ${len(months)}')
        datafile.write(f'Total: ${totalPr_Ls}')
        print(f'Total: ${totalPr_Ls}')
        datafile.write(f'Average Change: {round((int(first)-int(row[1]))/(len(months)-1),2)}')
        print(f'Average Change: {round((int(first)-int(row[1]))/(len(months)-1),2)}')
        datafile.write(f'Greatest Increase in Profits: {greatestInc[0]} $({greatestInc[1]})')
        print(f'Greatest Increase in Profits: {greatestInc[0]} $({greatestInc[1]})')
        datafile.write(f'Greatest Decrease in Profits: {greatestDec[0]} $({greatestDec[1]})')
        print(f'Greatest Decrease in Profits: {greatestDec[0]} $({greatestDec[1]})')

