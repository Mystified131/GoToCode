infile = open("MOD.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == ".":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("ModNo.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == ".":
            bline+=y
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

print(A2)

outlst = []

for elem in A2:
    try:
        anum = int(elem)
        astr = A1[anum]
        outlst. append(astr)
    except:
        anum == 0

outfile = open("scriptsb.txt", "w")

for elem in outlst:
    outfile.write(elem +  '\n')

outfile.close()


