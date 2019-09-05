infile = open("Col1.txt", "r")

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

outfile = open("scripts.txt", "w")

for elem in A1:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        




