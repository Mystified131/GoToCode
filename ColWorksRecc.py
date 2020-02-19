infile = open("Rec.txt", "r")

A1 = []

listref = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlsta = []



for elem in A1:
    for x in range(7):
        outlsta.append(elem)


outfile = open("scriptsa.txt", "w")

for elem in outlsta:
    outfile.write(elem +  '\n')

outfile.close()
