infile = open("1.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == " ":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("2.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == " ":
            bline+=y
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("3.txt", "r")

A3 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == " ":
            bline+=y
    A3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()


outlst = []

x = len(A1)

for ctr in range(x):
    try:
        astr = A1[ctr]
        bstr = A2[ctr]
        cstr = A3[ctr]
        cstr = astr + "." + bstr + "." + cstr
        outlst.append(cstr)
    except:
        print("Finished.")

outfile = open("scriptsd.txt", "w")

for elem in outlst:
    outfile.write(elem +  '\n')

outfile.close()



