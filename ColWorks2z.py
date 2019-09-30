infile = open("RSizFri.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " ":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlst = []

for elem in A1:
    for x in range(8,16):
        if int(elem) == x:
            outlst.append("1")
        if int(elem) != x:
            outlst.append("0")

print(outlst)

outfile = open("scriptsrec.txt", "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        




