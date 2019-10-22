infile = open("Coat.txt", "r")

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


outlst = []
outlst2 = []

for elem in A1:
    astr = elem[:2]
    bstr = elem[2:]
    outlst.append(astr)
    outlst2.append(bstr)

outfile = open("scriptsrec.txt", "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()


outfile = open("scriptsrecb.txt", "w")

for elem in outlst2:
    
    outfile.write(elem +  '\n')

outfile.close()


print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        

