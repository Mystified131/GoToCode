infile = open("1.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("2.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("3.txt", "r")

A3 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    A3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("4.txt", "r")

A4 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    A4.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlst = []

x = len(A1)

for ctr in range(x):
    astr = "Update dbo.CondUnitBaaNData_CondensingUnit set AWEFPassOrFail = '" + A3[ctr] + "' where CondUnitModelID = " + A1[ctr] + " and RefType = '" + A2[ctr] + "';"
    bstr = "Update dbo.CondUnitBaaNData_CondensingUnit set AWEFRating = " + A4[ctr] + " where CondUnitModelID = " + A1[ctr] + " and RefType = '" + A2[ctr] + "';"
    outlst.append(astr)
    outlst.append(bstr) 

outfile = open("scriptsnew.txt", "w")

for elem in outlst:
    outfile.write(elem +  '\n')

outfile.close()

