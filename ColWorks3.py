infile = open("HMod.txt", "r")

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

outlst = []
outlstb = []

for elem in A1:
    outlst.append(elem)
    outlst.append(elem)
    outlstb.append('7')
    outlstb.append('10')


outfile = open("scriptsout.txt", "w")

for elem in outlst:
    outfile.write(elem +  '\n')

outfile.close()

outfile = open("scriptsoutb.txt", "w")

for elem in outlstb:
    outfile.write(elem +  '\n')

outfile.close()