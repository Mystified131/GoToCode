infile = open("a.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == " ":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("b.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == " ":
            bline+=y
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

x = len(A1)

outlst = []

for ctr in range(x):
    if A2[ctr] == 'NULL':
        astr = "UPDATE dbo.CondUnitBaaNData set AWEFPassOrFail = 'Exempt' WHERE CondUnitBaaNDataId = " + str(ctr) + ";"
        bstr = "UPDATE dbo.CondUnitBaaNData set AWEFRating = 'Exempt' WHERE CondUnitBaaNDataId = " + str(ctr) + ";"
        outlst.append(astr)
        outlst.append(bstr)


outfile = open("scriptsa2.txt", "w")

for elem in outlst:
    outfile.write(elem +  '\n')

outfile.close()



