import csv
import datetime
from subprocess import call

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

#This code takes in the necessary arguments

print("")

print("Welcome to Table Populator")

print("")

tbl = input("Please enter the name of the table to populate: ")

print("")

val = input("Please enter the name of the .csv file, without the .csv suffix. Please eliminate any headers: ")

print("")

valin = val  + ".csv"

try:
    with open(valin, 'r') as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=',')
        for row in csv_reader:
            colnum=len(row)

except:
    print("")
    print("No file by that name can be found.")
    call(["python", "RowAdder.py"])


strlst = []

for x in range(colnum):
    yn = input("Is column number " + str(x) + " a string? If so, enter a '1': ")
    print("")
    if yn == "1":
        strlst.append(1)
    if yn != "1":
        strlst.append(0)

outfil = tbl + tim + ".csv"

with open(valin, newline='\n') as f_input, open(outfil, 'w', newline='\n') as f_output:

    csv_input = csv.reader(f_input)
    csv_output = csv.writer(f_output)

    

    for row in csv_input:

        outlst = []

        astr = 'INSERT INTO ' + tbl + " VALUES ("

        outlst.append(astr)

        for x in range(colnum):
            astr = row[x]

            if strlst[x] == 1:
                bstr= "'" + astr + "'"

            if strlst[x] != 1:
                bstr = astr

            if x < (colnum-1):
                outlst.append(bstr)
                outlst.append(",")

            if x == (colnum-1):
                outlst.append(bstr)
                outlst.append(");") 

        csv_output.writerow(outlst)  

print("Your file can be found in this directory.")

    

