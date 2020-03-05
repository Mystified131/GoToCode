import csv
import datetime
from subprocess import call

#CM.csv = All tables and columns from Comp_M
#RS.csv = All tables and columns from RS_CondUnit

#use sql:

 #SELECT T.name AS Table_Name ,
#       C.name AS Column_Name ,
#       P.name AS Data_Type ,
#       P.max_length AS Size ,
#       CAST(P.precision AS VARCHAR) + '/' + CAST(P.scale AS VARCHAR) AS Precision_Scale
#FROM   sys.objects AS T
#       JOIN sys.columns AS C ON T.object_id = C.object_id
#       JOIN sys.types AS P ON C.system_type_id = P.system_type_id
#WHERE  T.type_desc = 'USER_TABLE'

#Order by Table_Name;

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

#This code gets necessary arguments from the user

print ("")
print ("Welcome.")
print ("")

tablename = "Condensing Unit Study"

#tablename = input("Please type a name to designate both tables: ")
#print ("")
#colone = input("How many columns has the first table?: ")
#print ("")

#This code retrieves data from the first csv file

#coloneint = int(colone)

filenamesone = []

#filnm = ""
#filnma = ""
#filnma = input("What is the name of the file containing the data from the first (Comp M) table, without the .csv suffix: ")

filnma = 'CM'

filnm = filnma + ".csv"

print("")

try: 
    infile = open(filnm, "r")

except:
    print("No such csv file was found in this directory.")
    call(["python", "2CSVDeltas.py"])


totlst = []

aline = infile.readline()
while aline:

        totlst.append(aline)
        aline = infile.readline()
infile.close()



#This code retrieves data from the second csv file and finds and lists deltas between the two

rowoneint = len(totlst)

#filnm2 = ""
#filnm2a = ""
#filnm2a = input("What is the name of the file containing the data from the second (RS) table, without the csv suffix: ")

filnm2a = 'RS'

filnm2 = filnm2a + ".csv"

try: 
    infile = open(filnm2, "r")

except:
    print("")
    print("No such csv file was found in this directory.")
    call(["python", "2CSVDeltas.py"])

infile.close()

deltarows = []
deltacols = []
deltalistone = []
deltalisttwo = []

c =0
field={}

testlst = []
testlst2 = []
lena = ""
lenb = ""

with open(filnm, 'r') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    for row in csv_reader:
        astr = str(row)
        if ('_CondensingUnit' in astr or '_condensingUnit' in astr) and ('TEMP' not in astr):
            testlst.append(row)


with open(filnm2, 'r') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    for row in csv_reader:
        if 'TEMP' not in str(row):
            testlst2.append(row)

outfile = open("scripts1.txt", "w")

for elem in testlst:
    outfile.write(str(elem) +  '\n')

outfile.close()

outfile = open("scripts2.txt", "w")

for elem in testlst2:
    outfile.write(str(elem) +  '\n')

outfile.close()

lsta = []
lsta2 = []
lsta3 = []
lsta4 = []

for elem in testlst:
    astr = elem[0]
    bstr = elem[1]
    cstr = elem[2]
    dstr = elem[3]
    lsta.append(astr)
    lsta2.append(bstr)
    lsta3.append(cstr)
    lsta4.append(dstr)

lstb = []
lstb2 = []
lstb3 = []
lstb4 = []

for elem in testlst2:
    astr = elem[0]
    bstr = elem[1]
    cstr = elem[2]
    dstr = elem[3]
    lstb.append(astr)
    lstb2.append(bstr)
    lstb3.append(cstr)
    lstb4.append(dstr)

inbotlst = []
in2lst = []
in1lst = []

x = len(lstb)

for ctr in range(x):
    astr = lstb[ctr]
    colstr = lstb2[ctr]
    a2str = astr + "_CondensingUnit"
    print(a2str)
    bstr = lstb[ctr] + "." + lstb2[ctr] + "." + lstb3[ctr] + "." + lstb4[ctr]
    if a2str in lsta and colstr in lsta2 and bstr not in inbotlst:        
        inbotlst.append(bstr)
    if a2str not in lsta and bstr not in in2lst:
        in2lst.append(bstr)
    if colstr not in lsta2 and bstr not in in2lst:
        in2lst.append(bstr)

x = len(lsta)

for ctr in range(x):
    astr = lsta[ctr]
    colstr = lsta2[ctr]
    a2str = astr[:-15]
    print(a2str)
    bstr = lsta[ctr] + "." + lsta2[ctr] + "." + lsta3[ctr] + "." + lsta4[ctr]
    if a2str not in lstb and bstr not in in1lst:
        in1lst.append(bstr)
    if colstr not in lstb2 and bstr not in in1lst:
        in1lst.append(bstr)

outfile = open("scriptsreport.txt", "w")

outfile.write('' +  '\n')

outfile.write('In Components_M, but not in Rulestream:' +  '\n')

outfile.write('' +  '\n')

for elem in in1lst:
    outfile.write(elem +  '\n')

outfile.write('' +  '\n')

outfile.write('In Rulestream, but not in Components_M:' +  '\n')

outfile.write('' +  '\n')

for elem in in2lst:
    outfile.write(elem +  '\n')

outfile.write('' +  '\n')

outfile.write('In both tables:' +  '\n')

outfile.write('' +  '\n')

for elem in inbotlst:
    outfile.write(elem +  '\n')

outfile.close()


  