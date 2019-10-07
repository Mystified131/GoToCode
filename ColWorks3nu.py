infile = open("1a.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("1b.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

EvDic = {}

x = len(A1)

for ctr in range(x):
    EvDic[A2[ctr]] = A1[ctr]

infile = open("2a.txt", "r")

A3 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    A3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("2b.txt", "r")

A4 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    if bline.startswith("L"):        
        cline = bline[:4] + " " + bline[4:]
        A4.append(cline)
    if not bline.startswith("L"): 
        A4.append(bline) 
    
    bline = ""
    aline = infile.readline()
infile.close()


x = len(A3)

for ctr in range(x):
    EvDic[A4[ctr]] = A3[ctr]

infile = open("3a.txt", "r")

A5 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    A5.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("3b.txt", "r")

A6 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    cline = bline[:2] + bline[4:-1]
    A6.append(cline)
    bline = ""
    aline = infile.readline()
infile.close()


x = len(A1)

for ctr in range(x):
    EvDic[A6[ctr]] = A5[ctr]

print(EvDic)

infile = open("PType.txt", "r")

A7 = []
A8 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " ":
            bline+=y
    A7.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outfile = open("scriptsout1.txt", "w")

for elem in EvDic:
    outfile.write(elem +  '\n')

outfile.close()

outfile = open("scriptsout2.txt", "w")

for elem in EvDic:
    astr = EvDic[elem]
    outfile.write(astr +  '\n')

outfile.close()

print(A7)

outmod = []

for elem in A7:
    if elem in EvDic.keys():
        astr = EvDic[elem]
        outmod.append(astr)
    if elem not in EvDic:
        outmod.append("NULL")

outfile = open("scriptsout3.txt", "w")

for elem in outmod:
    outfile.write(elem +  '\n')

outfile.close()
