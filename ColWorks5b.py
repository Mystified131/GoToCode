infile = open("FLMod.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
        cline = bline[4:9]
    A1.append(cline)
    bline = ""
    cline = ""
    aline = infile.readline()
infile.close()

print(A1)

A2 = []

for x in range(1,92):
    A2.append(str(x))


outfile = open("scriptsFL2.txt", "w")

for elem in A2:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        
