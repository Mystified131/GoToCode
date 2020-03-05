infile = open("1a.txt", "r")

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

infile = open("1b.txt", "r")

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

infile = open("1c.txt", "r")

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

infile = open("1d.txt", "r")

A4 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    A4.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("1e.txt", "r")

A5 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-" or y == "_":
            bline+=y
    A5.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlsta = []
outlstb = []
outlstc = []
outlstd = []
outlste = []

x = len(A1)

for ctr in range(x):
    astr = A3[ctr]
    if 'NA' not in astr:
        outlsta.append(A1[ctr])
        outlstb.append(A2[ctr])
        outlstc.append(A3[ctr])
        outlstd.append(A4[ctr])
        outlste.append(A5[ctr])
 
outfile = open("scriptsa.txt", "w")

for elem in outlsta:
    outfile.write(elem +  '\n')

outfile.close()

 
outfile = open("scriptsb.txt", "w")

for elem in outlstb:
    outfile.write(elem +  '\n')

outfile.close()

 
outfile = open("scriptsc.txt", "w")

for elem in outlstc:
    outfile.write(elem +  '\n')

outfile.close()

 
outfile = open("scriptsd.txt", "w")

for elem in outlstd:
    outfile.write(elem +  '\n')

outfile.close()

 
outfile = open("scriptse.txt", "w")

for elem in outlste:
    outfile.write(elem +  '\n')

outfile.close()


