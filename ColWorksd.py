infile = open("Ref.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == ".":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlst = []

for elem in A1:
    if elem == "MS":
        outlst.append("R404A")
    if elem == "MQ":
        outlst.append("R407A")
    if elem == "MT":
        outlst.append("R448A")
    if elem == "MR":
        outlst.append("R449A")
    if elem == "MF":
        outlst.append("R407F")
    if elem == "MP":
        outlst.append("R507")
    if elem == "LS":
        outlst.append("R404A")
    if elem == "LP":
        outlst.append("R507")
    if elem == "LQ":
        outlst.append("R407A")
    if elem == "LT":
        outlst.append("R448A")
    if elem == "LR":
        outlst.append("R449A")
    if elem == "LF":
        outlst.append("R407F")

outfile = open("scriptsrec.txt", "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        

