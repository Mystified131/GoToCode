infile = open("scripts3.txt", "r")

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
    if "8  5/8 x 28" in elem:
        outlst.append("A")
    if "8  5/8 x 48" in elem:
        outlst.append("B")
    if "8  5/8 x 60" in elem:
        outlst.append("C")
    if "10 3/4 x 48" in elem:
        outlst.append("D")
    if "10 3/4 x 72" in elem:
        outlst.append("E")
    if "10 3/4 x 96" in elem:
        outlst.append("F")
    if "10 3/4 x 10" in elem:
        outlst.append("G")
    if "10 3/4 x 14" in elem:
        outlst.append("H")

    if "8  5/8 x 48" not in elem and "10 3/4 x 10" not in elem and "8  5/8 x 28" not in elem and "8  5/8 x 60" not in elem and "10 3/4 x 48" not in elem and "10 3/4 x 72" not in elem and "10 3/4 x 96" not in elem and "10 3/4 x 14" not in elem:
        outlst.append("0")



outfile = open("scripts6.txt", "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        




