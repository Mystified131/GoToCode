import datetime

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

infile = open("Val.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == ".":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlst = []

for elem in A1:
    if elem:
        outlst.append(elem)
    if not elem:
        outlst.append("NULL")

afil = "ColWorks" + tim + ".txt"

outfile = open(afil, "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The output txt file should now be available in the same folder as the python code.")        

