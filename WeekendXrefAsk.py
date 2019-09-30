
import csv

#This code creates the SQL data to drop values from a .csv into the table

valin = "Weekend.csv"

with open(valin, 'r') as csvFile:
    rownum = 0
    csv_reader = csv.reader(csvFile, delimiter=',')
    for row in csv_reader:
        rownum += 1
        colnum=len(row)

vallst = []

for ctr in range(colnum):

    with open(valin) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            x1 = row[ctr]            
            #if cnnm > 0:
            vallst.append(x1) 

print(vallst)

outfile = open("scriptsrec.txt", "w")

for elem in vallst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        
