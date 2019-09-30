infile = open("Notes.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/"  or y == "*" or y == " ":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("Models.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "*" or y == " ":
            bline+=y
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

print(A1)

alst = []
blst = []
clst = []
dlst = []

for elem in A1:
    astr = elem[:10]
    bstr = elem[13:18]
    cstr = elem[19:24]
    dstr = elem[25:36]
    alst.append(astr)
    blst.append(bstr)
    clst.append(cstr)
    dlst.append(dstr)

print(alst)
print(blst)
print(clst)
print(dlst)

x = len(A1)

bdic = {}
cdic = {}
ddic = {}

for ctr in range(x):
    bdic[alst[ctr]] = blst[ctr]
    cdic[alst[ctr]] = clst[ctr]
    ddic[alst[ctr]] = dlst[ctr]

print(bdic)
print(cdic)
print(ddic)

endlst = []
endlst2 = []
endlst3 = []

for elem in A2:
    tstr = elem[0:2]
    sstr = elem[3:8]
    ctr = 0
    for elem2 in alst:
        if tstr in elem2 and sstr in elem2 and ctr == 0:
            print(tstr)
            print(sstr)
            endlst.append(bdic[elem2])
            endlst2.append(cdic[elem2])
            endlst3.append(ddic[elem2])
            ctr = 1
    if ctr == 0:
        endlst.append('0')
        endlst2.append('0')
        endlst3.append('0')
        
print(endlst)
print(endlst2)
print(endlst3)

outfile = open("scripts.txt", "w")

for elem in endlst:
    
    outfile.write(elem +  '\n')

outfile.close()

outfile = open("scripts2.txt", "w")

for elem in endlst2:
    
    outfile.write(elem +  '\n')

outfile.close()

outfile = open("scripts3.txt", "w")

for elem in endlst3:
    
    outfile.write(elem +  '\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")        


