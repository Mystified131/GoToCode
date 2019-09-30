infile = open("FCMod.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/":
            bline+=y
        if y == "*":
            bline+="H"
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("FCMod.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/":
            bline+=y
        if y == "*":
            bline+="C"
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("FCMod.txt", "r")

A3 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/":
            bline+=y
        if y  == "*":
            bline+="E"
    A3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("FCMod.txt", "r")

A4 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/":
            bline+=y
        if y == "*":
            bline+="F"
    A4.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outfile = open("scriptsfc.txt", "w")

for elem in A1:    

    outfile.write(elem +  '\n')

for elem in A2:    

    outfile.write(elem +  '\n')

for elem in A3:    

    outfile.write(elem +  '\n')

for elem in A4:    

    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        


