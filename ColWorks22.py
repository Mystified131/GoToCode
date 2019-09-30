infile = open("scripts.txt", "r")

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
    if "7/8" in elem:
        outlst.append("A")
    if "1 1/8" in elem:
        outlst.append("B")
    if "1 3/8" in elem:
        outlst.append("C")
    if "1 5/8" in elem:
        outlst.append("D")


    if "7/8" not in elem and "1 1/8" not in elem and "1 3/8" not in elem and "1 5/8" not in elem:
        outlst.append("0")



outfile = open("scripts4.txt", "w")

for elem in outlst:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        




