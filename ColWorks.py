infile = open("comp.txt", "r")

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

outval = ""

for elem in A1:
    if elem == "Nomatch":
        outval = "999999"
        outlst.append(outval)
    if elem != "Nomatch":
        outlst.append(elem)

print(outlst)

outfile = open("scripts.txt", "w")

x = len(outlst)

for ctr in range(x):
    
    outstr = "Update dbo.CondensingUnitModel_CondensingUnit SET CompressorModelID = " + outlst[ctr] + " WHERE CondUnitModelID = " + str(ctr + 1) + ";"

    outfile.write(outstr +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        




