import csv

#This code gets necessary arguments from the user

print ("")
print ("Welcome to the table comparison tool.")
print ("")
tablename = input("Please type a name to designate both tables: ")
print ("")
#colone = input("How many columns has the first table?: ")
#print ("")

#This code retrieves data from the first csv file

#coloneint = int(colone)

filenamesone = []

filnm = ""
filnma = ""
filnma = input("What is the name of the file containing the data from the first table, without the .csv suffix: ")

filnm = filnma + ".csv"

print("")

infile = open(filnm, "r")

totlst = []

aline = infile.readline()
while aline:
        totlst.append(aline)
        aline = infile.readline()
infile.close()

#This code retrieves data from the second csv file and finds and lists deltas between the two

rowoneint = len(totlst)

filnm2 = ""
filnm2a = ""
filnm2a = input("What is the name of the file containing the data from the second table, without the csv suffix: ")

filnm2 = filnm2a + ".csv"

deltarows = []
deltacols = []
deltalistone = []
deltalisttwo = []

c =0
field={}

with open(filnm, 'r') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    for row in csv_reader:
        colone1int=len(row)

with open(filnm2, 'r') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    for row in csv_reader:
        colone2int=len(row)

if colone1int >= colone2int:
    coloneint = colone2int

if colone1int < colone2int:
    coloneint = colone1int

for ctr in range(coloneint):

    with open(filnm) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        onecoldata = []
            #cnnm = 0
        for row in csv_reader:
            x1 = row[ctr]            
            #if cnnm > 0:
            onecoldata.append(x1) 
             #cnnm += 1

        onecoldata = [ i.lstrip('0') for i in onecoldata ]

    with open(filnm2) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        onecoldata2 = []
        #cnnm = 0
        for row in csv_reader:
            x1 = row[ctr]
            #if cnnm > 0:
            onecoldata2.append(x1) 
            #cnnm += 1

        onecoldata2 = [ i.lstrip('0') for i in onecoldata2 ]

    cotr = ctr + 1
    x = len(onecoldata)
    for elem in range(x):
        if type(onecoldata[elem]) == str or type(onecoldata2[elem]) == str:
            if onecoldata[elem] != onecoldata2[elem]:
                rowstr = str(elem+1)
                deltarows.append(rowstr)
                colstr = str(cotr)
                deltacols.append(colstr)
                deltalistone.append(onecoldata[elem])
                deltalisttwo.append(onecoldata2[elem])


        else:
            valone = float(onecoldata[elem])
            valtwo = float(onecoldata2[elem])
            if valone != valtwo:
                valoneb = round(valone, 5)
                valtwob = round(valtwo, 5)
                rowstr = str(elem+1)
                deltarows.append(rowstr)
                colstr = str(cotr)
                deltacols.append(colstr)
                deltalistone.append(valoneb)
                deltalisttwo.append(valtwob)
        ""

#This code creates a report of deltas between the two tables

outname = tablename + "_report.txt"
outfile = open(outname, "w")
outfile.write("Report for " + tablename + '\n')
outfile.write('\n')

if colone1int == colone2int:
    outfile.write("There are no deltas in column numbers." + '\n')
    outfile.write('\n')
if colone1int != colone2int:
    outfile.write("There are deltas in column numbers." + '\n')
    outfile.write('\n')
    astr = str(colone1int)
    bstr = str(colone2int)
    outfile.write("Table 1 has " + astr + " columns." + '\n')
    outfile.write("Table 2 has " + bstr + " columns." + '\n')
    outfile.write('\n')
    
x = len(deltarows)

x1 = str(x)

outfile.write("There are a total of " + x1 + " deltas between the two tables." + '\n')
outfile.write('\n')

if x > 0:
    for elem in range(x):
        repstr = str("Column Number: " + str(deltacols[elem])  +  '\n' + "Row Number: " + str(deltarows[elem])  +  '\n' + "First Table: " + str(deltalistone[elem]) + " Second Table: " + str(deltalisttwo[elem]))
        outfile.write(repstr + '\n')
        outfile.write('\n')   
else:
    outfile.write("The tables have identical data. Thank you." '\n')
    outfile.write('\n')
        
outfile.close()

print("")
print("You will find your report file in the same folder as this code. Thank you.")
