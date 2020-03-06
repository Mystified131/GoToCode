#A1a - CompRefType (ie 33.F.M or 101.S.L) / A2a = UnitType from AWEF table-- only using "D" units / A3a = AWEF

infile = open("A1a.txt", "r")

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

#infile = open("A2a.txt", "r")

#A1b = []

#aline = infile.readline()

#bline = ""

#while aline:
#    for y in aline:
#        if y.isalnum() or y == "/" or y == "." or y == "-":
#            bline+=y
 #   A1b.append(bline)
#    bline = ""
 #   aline = infile.readline()
#infile.close()

infile = open("A3a.txt", "r")

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

WEFFdict = {}

x = len(A1a)

for ctr in range(x):
#    astr = A1b[ctr]
#    if astr == 'D':
    astr = A1a[ctr]
    bstr = A1c[ctr]
    WEFFdict[astr] = bstr

print(WEFFdict)

#CB1a - CondUnitModel# / CB2a - CompRefType ( ie 33.F.M or 101.S.L ) from Model Xref Table

infile = open("B1a.txt", "r")

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

infile = open("B2a.txt", "r")

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

MODDict = {}

x = len(B1a)

for ctr in range(x):
    astr = B1a[ctr]
    bstr = B1b[ctr]
    MODDict[astr] = bstr

print(MODDict)

totdict = {}

for elem in MODDict:
    try:
        astr = WEFFdict[MODDict[elem]]
        totdict[elem] = astr
    except:
        print("Key Mismatch")

print(totdict)

outlst = []

for elem in B1a:
    try:
        outlst.append(totdict[elem])
    except:
        outlst.append('NULL')

outfile = open("scriptsweff.txt", "w")

for elem in outlst:
    outfile.write(elem +  '\n')

outfile.close()        


