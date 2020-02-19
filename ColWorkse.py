infile = open("HDat.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "." or y == "-" or y == "#":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlst = []
outlstb = []
outlstc = []
outlstd = []
outlste = []
outlstf = []
outlstg = []

for elem in A1:
    astr = elem[:16]
    outlst.append(astr)
    bstr = elem[16:24]
    outlstb.append(bstr)
    cstr = elem[23:25]
    j = 0
    for x in cstr:
        if x == "S" or x == "M" or x == "L" or x == "X" and j == 0:
            outlstc.append(x)
            j = 1
    if "S" not in cstr and "M" not in cstr and "L" not in cstr and "X" not in cstr  :
        outlstc.append(cstr)
    dstr = elem[25:27]
    j = 0
    for x in dstr:
        if x == "S" or x == "M" or x == "L" or x == "X" and j == 0:
            outlstd.append(x)
            j = 1
    if "S" not in dstr and "M" not in dstr and "L" not in dstr and "X" not in dstr  :
        outlstd.append(dstr)
    ctr = elem.find('LBS')
    numb = ctr + 3
    numc = numb + 16
    estr = elem[numb:numc]
    if ctr > 0:
        outlste.append(estr)
    if ctr == 0:
        outlste.append('NULL')

    ctr = elem.find('LBS')
    numb = ctr - 7
    fstr = elem[numb:ctr]
    if ctr > 0:
        outlstf.append(fstr)
    if ctr == 0:
        outlstf.append('NULL')

    ctr = elem.find('LBS')
    numb = ctr - 9
    numc = ctr - 7
    gstr = elem[numb:numc]
    if ctr > 0:
        outlstg.append(gstr)
    if ctr == 0:
        outlstg.append('NULL')




outfile = open("scripts.txt", "w")

for elem in outlst:
    outfile.write(str(elem) +  '\n')

outfile.close()

outfile = open("scriptsb.txt", "w")

for elem in outlstb:
    outfile.write(str(elem) +  '\n')

outfile.close()

outfile = open("scriptsc.txt", "w")

for elem in outlstc:
    outfile.write(str(elem) +  '\n')

outfile.close()

outfile = open("scriptsd.txt", "w")

for elem in outlstd:
    outfile.write(str(elem) +  '\n')

outfile.close()

outfile = open("scriptse.txt", "w")

for elem in outlste:
    outfile.write(str(elem) +  '\n')

outfile.close()

outfile = open("scriptsf.txt", "w")

for elem in outlstf:
    outfile.write(str(elem) +  '\n')

outfile.close()

outfile = open("scriptsg.txt", "w")

for elem in outlstg:
    outfile.write(str(elem) +  '\n')

outfile.close()



