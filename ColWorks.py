infile = open("1.txt", "r")

A1 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    cline = bline[:-1]
    A1.append(cline)
    dline = bline[-1:]
    listref.append(dline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("2.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "."  or y == "-" :
            bline+=y
    cline = bline[:-1]
    A2.append(cline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("3.txt", "r")

A3 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." :
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
        if y.isalnum() or y == "/" or y == "." :
            bline+=y
    A4.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

Moddic = {}

x = len(A2)

for ctr in range(x):
    Moddic[A2[ctr]] = str(ctr)

print(Moddic)

print(A1)

x = len(A2)

listid = []

for elem in A1:
    try:
        astr = Moddic[elem]
        listid.append(astr)
    except:
        listid.append('NULL')

print(listid)

print(listref)

x = len(A3)

outlst = []

for ctr in range(x):
    astr = "UPDATE dbo.CondUnitBaaNData Set AWEFPassOrFail = '" + A3[ctr] + "' WHERE CondUnitModelID = " + listid[ctr] + " and RefType = '" + listref[ctr] + "';"
    bstr = "UPDATE dbo.CondUnitBaaNData Set AWEFRating = '" + A4[ctr] + "' WHERE CondUnitModelID = " + listid[ctr] + " and RefType = '" + listref[ctr] + "';"
    outlst.append(astr)
    outlst.append(bstr)

outfile = open("scriptsa.txt", "w")

for elem in outlst:
    outfile.write(elem +  '\n')

outfile.close()

