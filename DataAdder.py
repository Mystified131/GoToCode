
import csv
import datetime

#This code takes in the necessary arguments

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

strlst = []
namlst = []

print("")

print("Welcome to Table Populator")

print("")

tbl = input("Please enter the name of the table to populate: ")

print("")

val = input("Please enter the name of the .csv file, without the .csv suffix. Please eliminate any headers: ")

print("")

colnum = input("How many columns are there to populate? Note that, if the primary key column is also referenced, that counts as a column, so please add 1 to your total: ")

print("")

valcol = input("Please enter the name of the primary key column holding values: ")

print("")

namlst.append(valcol)

primcoldata = input("Please enter '1' if the data input is a string, '0' if not: ")

print("")

if primcoldata == "1":
    strlst.append(1)

if primcoldata != "1":
    strlst.append(0)

primdat = int(primcoldata)

#This code creates the SQL data to drop values from a .csv into the table

valin = val + ".csv"

valot = tbl + tim + ".csv"

colnm = (int(colnum)-1)
for x in range(colnm):

    valcolx = input("Please enter the name of a column holding values: ")

    print("")

    namlst.append(valcolx)

    valcoldatax = input("Please enter '1' if the data input is a string: ")

    print("")

    if valcoldatax == "1":
        strlst.append(1)

    if valcoldatax != "1":
        strlst.append(0)

with open(valin, newline='\n') as f_input, open(valot, 'w', newline='\n') as f_output:

    csv_input = csv.reader(f_input)
    csv_output = csv.writer(f_output)

    for row in csv_input:

        outlst = []

        for x in range(1, int(colnum)):

            xstr = "ALTER " + tbl + " SET "
            
            outlst.append(xstr)
            
            ystr = namlst[x]
            
            outlst.append(ystr)
            
            zstr = " = "

            outlst.append(zstr)

            ostr = row[x]
            nstr = row[0]
            nnam = namlst[0]

            if strlst[x] == 1:
                bstr= "'" + ostr + "'"

            if strlst[x] != 1:
                bstr = ostr

            outlst.append(bstr)

            xxstr = " WHERE "

            outlst.append(xxstr)

            yystr = nnam + " = " 

            outlst.append(yystr)

            zzstr =  nstr

            outlst.append(zzstr)

            zzzstr = ";"

            outlst.append(zzzstr)        

        csv_output.writerow(outlst)  

print ("The scripts file should now be available in the same folder as the python code.")
