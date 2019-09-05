

import csv

#This code takes in the necessary arguments

print("")

print("Welcome to Table Populator")

print("")

tbl = input("Please enter the name of the table to populate: ")

print("")

val = input("Please enter the name of the .csv file, without the .csv suffix. Please eliminate any headers: ")

print("")

valin = val  + ".csv"

with open(valin, 'r') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    for row in csv_reader:
        colnum=len(row)

filtxt = "popscript" + ".txt"

outfile = open(filtxt, "w")

colnmm = int(colnum)

addlst = []

addst = "INSERT INTO " + tbl +  " VALUES (" 

for x in range(colnmm):

    print("Please go to a column holding values.")

    print("")

    valcoldatax = input("Please enter '1' if the data input is a string, '0' if not: ")

    print("")

    valcolnum = input("Please enter which column (starting with 0) those values belong to on the original .csv: ")

    valcolnumint = int(valcolnum)

    print("")

    vallst = []

    with open(valin) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            x1 = row[valcolnumint]            
            vallst.append(x1) 

    if x == 0:

        for elem in vallst:

            if valcoldatax == "1":
                eleme = "'" + elem + "'"
            else:
                eleme = elem

            addst = "INSERT INTO " + tbl +  " VALUES ( " + eleme + ", "
            addlst.append(addst)

    if x > 0:

        ctr = len(vallst)
        for x1 in range(ctr):
            str1 = addlst[x1]
            vall = vallst[x1]
            if valcoldatax == "1":
                valle = "'" + vall + "'"
            else:
                valle = vall
            nustr = str1 + valle + ", "
            addlst[x1] = nustr

finlst = []

for elem in addlst:
    chstr = elem[:-2]
    chstr += " );"
    finlst.append(chstr)

for elem in finlst:
    outfile.write(elem + '\n')
    outfile.write('\n')

outfile.close()

print("Your file is listed as 'popscript', and can be found in this directory.")

    

