infile = open("Typ.txt", "r")

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

infile = open("RL1.txt", "r")

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

infile = open("RL2.txt", "r")

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


outlsta = []

x = len(A1)

for ctr in range(x):
    if A1[ctr] not in ['NULL', '1', '2', '3', '4']:
        outlsta.append(A3[ctr])
    if A1[ctr] in ['NULL', '1', '2', '3', '4']:
        outlsta.append(A2[ctr])



outfile = open("scriptsa.txt", "w")

for elem in outlsta:
    outfile.write(elem +  '\n')

outfile.close()


