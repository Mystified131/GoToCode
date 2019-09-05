
import csv

#This code takes in the necessary arguments

print("")

print("Welcome to Table Populator")

print("")

tbl = input("Please enter the name of the table to populate: ")

print("")

val = input("Please enter the name of the .csv file, without the .csv suffix. Please eliminate any headers: ")

print("")

colnum = input("How many columns are there to populate? Note that, if the primary key column is also referenced, that counts as a column, so please add 1 to your total: ")

print("")

filtxt = "popscript" + ".txt"

outfile = open(filtxt, "w")


valcol = input("Please enter the name of the primary key column holding values: ")

print("")

primcoldata = input("Please enter '1' if the data input is a string, '0' if not: ")

print("")

valcolnum = input("Please enter which column (starting with 0) those values belong to on the original .csv: ")

valcolnumint = int(valcolnum)

primdat = int(primcoldata)

print("")

#This code creates the SQL data to drop values from a .csv into the table

val0lst = []

valin = val  + ".csv"

with open(valin) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            x1 = row[valcolnumint]            
            #if cnnm > 0:
            val0lst.append(x1) 

vallst = []

colnm = (int(colnum)-1)
for x in range(colnm):

    x2 = x + 1

    valcolx = input("Please enter the name of a column holding values: ")

    print("")

    valcoldatax = input("Please enter '1' if the data input is a string, '0' if not: ")

    print("")

    valcolnum = input("Please enter which column (starting with 0) those values belong to on the original .csv: ")

    valcolnumint = int(valcolnum)

    print("")

    #This code generates an output file with the necessary commands

    with open(valin) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            x1 = row[valcolnumint]            
            #if cnnm > 0:
            vallst.append(x1) 

        for row in csv_reader:
            x1 = row[0]            
            #if cnnm > 0:
            val0lst.append(x1) 


        x = len(vallst)
        for y in range(x):

            if valcoldatax == "1":
                addstr = "'" + vallst[y] + "'"
            else:
                addstr = vallst[y]
            if primcoldata == "1":
                valcol = "'" + valcol + "'"
            else:
                addrstr = vallst[y]
                       
            valcolm0 = val0lst[y]
            
            if len(addstr) > 0:
                op2str = "UPDATE " + tbl + " SET " + valcolx + " = " + addstr + " WHERE " + valcol + " =  " + valcolm0 + ";"
                outfile.write(op2str +  '\n')
                outfile.write( '\n')

    vallst = []

outfile.close()

print ("The scripts file should now be available in the same folder as the python code.")
