infile = open("pval.txt", "r")

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

infile = open("modkr.txt", "r")

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


infile = open("modrul.txt", "r")

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


infile = open("idrul.txt", "r")

A4 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    A4.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

x = len(A1)

pivdic = {}

for ctr in range(x):
    pivdic[A2[ctr]] = A1[ctr]

outlst = []

x = len(A3)

for ctr in range(x):
    if A3[ctr] in pivdic:
        vala = pivdic[A3[ctr]]
        if pivdic[A3[ctr]] == "NA":
            vala = "NULL"   
        outlst.append(vala)
    if A3[ctr] not in pivdic:
        vala = "NULL"
        outlst.append(vala)

print(outlst)


outfile = open("scripts.txt", "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        




