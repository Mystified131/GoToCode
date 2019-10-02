infile = open("ModID.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == " ":
            bline+=y
        if y == "-":
            bline+=" "
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlst = []

infile = open("ModRS.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == " ":
            bline+=y
        if y == "-":
            bline+=""
    cline = bline[:7]
    dline = cline[:2] + cline[3:]

    A1.append(dline)
    bline = ""
    aline = infile.readline()
infile.close()

print(A1)
print(A2)

moddic = {}

x = len(A1)

for ctr in range(x):
    moddic[A1[ctr]] = A2[ctr]

print(moddic)

infile = open("ModKrack.txt", "r")

A3 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " ":
            bline+=y
    A3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

print(A3)

outlst = []

for elem in A3:
    elm = elem[:6]
    print(elm)
    if elm in moddic:
        outlst.append(moddic[elm])
    if elm not in moddic:
        outlst.append("NULL")

print(outlst)

outfile = open("scriptskrk.txt", "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")  



