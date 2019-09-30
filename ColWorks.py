infile = open("Mod.txt", "r")

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

for elem in A1:
    achr = elem[5:6]
    if achr == "1":
        bchr = achr[6:8]
        if bchr == "81":
            outlst.append("9")
        if bchr != "81":
            outlst.append("8")
    if achr == "2":
        outlst.append("9")
    if achr == "3":
        bchr = achr[6:8]
        if bchr == "00":
            outlst.append("9")
        if bchr != "00":
            outlst.append("10")
    if achr == "4":
        outlst.append("10")
    if achr == "5":
        outlst.append("10")
    if achr == "6":
        bchr = achr[6:9]
        if bchr == "00M":
            outlst.append("11")
        if bchr == "01M":
            outlst.append("12")
        if bchr == "00L" or bchr == "02L":
            outlst.append("10")
        if bchr == "01L":
            outlst.append("11")
        if bchr != "00M" and bchr != "01M" and bchr != "00L" and bchr != "02L" and bchr != "01L":
            outlst.append("11")
    if achr == "7":
        outlst.append("12")
    if achr == "8":
        bchr = achr[6:8]
        if bchr == "00":
            outlst.append("12")
        if bchr != "00":
            outlst.append("13")
    

print(outlst)

outfile = open("scriptsrec.txt", "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        

