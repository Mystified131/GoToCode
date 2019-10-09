infile = open("Mod.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == "." or y == "-":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("Liq.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == "." or y == "-":
            bline+=y
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()


infile = open("Suc.txt", "r")

A3 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == "." or y == "-":
            bline+=y
    A3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

succon = []

x = len(A1)

for ctr in range(x):
    if A2[ctr] == "1/2":
        succon.append("250")
    if A2[ctr] == "5/8":
        succon.append("250")
    if A2[ctr] == "7/8":
        succon.append("250")
    if A2[ctr] != "1/2" and A2[ctr] != "5/8" and A2[ctr] != "7/8":
        succon.append(0)


outfile = open("scriptsrec.txt", "w")

for elem in succon:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        

sucfilnr = []

x = len(A1)

for ctr in range(x):
    if A3[ctr] == "5/8":
        sucfilnr.append("260")
    if A3[ctr] == "7/8":
        sucfilnr.append("220")
    if A3[ctr] == "1-1/8":
        sucfilnr.append("220")
    if A3[ctr] == "1-3/8":
        sucfilnr.append("230")
    if A3[ctr] == "1-5/8":
        sucfilnr.append("240")
    if A3[ctr] == "2-1/8":
        sucfilnr.append("260")
    if A3[ctr] != "5/8" and A3[ctr] != "7/8" and A3[ctr] != "1-1/8" and A3[ctr] != "1-3/8" and A3[ctr] != "1-5/8"  and A3[ctr] != "2-1/8":
        sucfilnr.append(0)


outfile = open("scriptsrecb.txt", "w")

for elem in sucfilnr:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        

