infile = open("CMods.txt", "r")

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

outdic = {}

for elem in A1:
    outdic[elem] = elem

outlst = []

for elem in outdic:
    outlst.append(elem)

print(outlst)

outfile = open("scriptsblue.txt", "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        




