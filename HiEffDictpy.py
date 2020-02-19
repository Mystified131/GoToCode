infile = open("HiweffModID.txt", "r")

A1a = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    A1a.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("HiweffType.txt", "r")

A1b = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    A1b.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("HiweffRef", "r")

A1c = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    A1c.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

A1 = []

x = len(A1a)

for ctr in range(x):
    astr = A1a[ctr] + A1b[ctr] + A1c[ctr]
    A1.append(astr)

print(A1)

infile = open("BaaNModID.txt", "r")

B1a = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    B1a.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("BaaNType.txt", "r")

B1b = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    B1b.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("BaaNRef.txt", "r")

B1c = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    B1c.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

A2 = []

x = len(B1a)

for ctr in range(x):
    astr = B1a[ctr] + B1b[ctr] + B1c[ctr]
    A2.append(astr)

print(A2)


infile = open("HiweffAWEF.txt", "r")

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

x = len(A3)

for ctr in range(x):
    Conddic[A1[ctr]] = A3[ctr]


print(Conddic)

outlst = []

for elem in A2:   
    try:
        astr = Conddic[elem]
        outlst.append(astr)
    except:
        outlst.append('NULL')


  

outfile = open("scriptsa.txt", "w")

for elem in outlst:
    astr = str(elem)
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scriptsb.txt", "w")
for elem in A1:
    astr = str(elem)
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scriptsc.txt", "w")
for elem in A2:
    astr = str(elem)
    outfile.write(astr +  '\n')

outfile.close()

