# To begin, provide a .txt file of the Tables by name, one per line, and tables in this form: t1.csv, t2.csv, and so on for all tables referenced

import csv
import datetime
from subprocess import call

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

infile = open("Tables.txt", "r")

tablelst = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    tablelst.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

x = len(tablelst)

for counter in range(x):

    tbl = tablelst[counter]

    val = 't' + str(counter+1)

    test = 'n'

    


    valin = val  + ".csv"


    with open(valin, 'r') as csvFile:
        csv_reader = csv.reader(csvFile, delimiter=',')
        for row in csv_reader:
            colnum=len(row)

    strlst = []

    for x in range(colnum):

        if test == "m":
            yn = input("Is column number " + str(x) + " a string? If so, enter a '1': ")
            print("")
            if yn == "1":
                strlst.append(1)
            if yn != "1":
                strlst.append(0)

        if test != 'm':

            content = []


            with open(valin, 'r') as csvFile:
                csv_reader = csv.reader(csvFile, delimiter=',')
                for row in csv_reader:
                    content.append(row[x])

            colstr = 0

            for elem in content:
                for x in elem:
                    if x.isalpha() and elem != 'NULL':
                        colstr = 1

            if colstr > 0:
                strlst.append(1)
            if colstr == 0:
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

                if astr != "":

                    if strlst[x] == 1 and astr != 'NULL':
                        bstr= "'" + astr + "'"

                    if strlst[x] != 1 or astr == 'NULL':
                        bstr = astr

                    if x < (colnum-1):
                        outlst.append(bstr)
                        outlst.append(",")

                    if x == (colnum-1):
                        outlst.append(bstr)
                        outlst.append(");") 

            csv_output.writerow(outlst)  

    outfil = tbl + tim + "NoID.csv"

    with open(valin, newline='\n') as f_input, open(outfil, 'w', newline='\n') as f_output:

        csv_input = csv.reader(f_input)
        csv_output = csv.writer(f_output)


        for row in csv_input:

            outlst = []

            astr = 'INSERT INTO ' + tbl + " VALUES ("

            outlst.append(astr)

            for x in range(colnum):

                astr = row[x]

                if astr != "":

                    if strlst[x] == 1 and astr != 'NULL':
                        bstr= "'" + astr + "'"

                    if strlst[x] != 1 or astr == 'NULL':
                        bstr = astr

                    if x < (colnum-1) and x != 0:
                        outlst.append(bstr)
                        outlst.append(",")

                    if x == (colnum-1):
                        outlst.append(bstr)
                        outlst.append(");") 

            csv_output.writerow(outlst)  

print("Your files can be found in this directory.")

            

