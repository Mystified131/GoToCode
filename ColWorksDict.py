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

Conddic = {}

x = len(A1)

for ctr in range(x):
    Conddic[A1[ctr]] = A2[ctr]


print(Conddic)

outlst = []

for elem in A3:
    if elem in A1:
        astr = Conddic[elem]
        outlst.append(astr)
    if elem not in A1:
        outlst.append('NULL')

outfile = open("scriptsa.txt", "w")

for elem in outlst:
    outfile.write(elem +  '\n')

outfile.close()

