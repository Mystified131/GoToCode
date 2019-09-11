infile = open("G.txt", "r")

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

vala = ""

outfile = open("scriptsWed.txt", "w")

for elem in A1:

    if elem == "NULL":
        vala = "0"
        outfile.write(vala +  '\n')
    if elem != "NULL":
        outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        




