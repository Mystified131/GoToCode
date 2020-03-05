infile = open("a1.txt", "r")

A1 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("a2.txt", "r")

A2 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("a3.txt", "r")

A3 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    A3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("b1.txt", "r")

B1 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    B1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("b2.txt", "r")

B2 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    B2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("b3.txt", "r")

B3 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    B3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("b4.txt", "r")

B4 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    B4.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

workdict = {}

x = (len(A1))

for ctr in range(x):
    try:
        astr = A1[ctr] + "." + A2[ctr]
        bstr = A3[ctr]
        workdict[astr] = bstr

    except:
        print("Limit reached.")
    

print(workdict)

workdict2 = {}

x = len(B1)

for ctr in range(x):
    try:
        astr = B1[ctr] + "." + "1"
        bstr = B2[ctr]
        workdict2[astr] = bstr

        cstr = B1[ctr] + "." + "4"
        dstr = B3[ctr]
        workdict2[cstr] = dstr

        estr = B1[ctr] + "." + "9"
        fstr = B4[ctr]
        workdict2[estr] = fstr

    except:
        print("Limit reached.")

print(workdict2)

anslst = []

for elem in workdict:
    try:
        resstr = "Components M- " + elem + ": " + workdict[elem] + " / Pricing Catalog- " + workdict2[elem]
    except: resstr = "Components M- " + elem + ": " + workdict[elem] + " / Pricing Catalog- " + "NULL"
    anslst.append(resstr)

print(anslst)

outfile = open("scriptsout.txt", "w")

for elem in anslst:
    outfile.write(elem +  '\n')

outfile.close()


















