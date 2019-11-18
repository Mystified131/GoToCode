infile = open("IDNew.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == ".":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlst = []
outlstb = []

for elem in A1:
    if elem[:1] == "0":
        outlst.append(elem)
        astr = elem[1:]
        outlstb.append(astr)

x = len(outlst)

outloss = []

for ctr in range(x):
    astr = "Update dbo.KitPartPricing_Pricing set KitPartNumber = '" + str(outlst[ctr]) + "' where KitPartNumber = '" + str(outlstb[ctr]) + "';"
    outloss.append(astr)


outfile = open("scriptsb.txt", "w")

for elem in outloss:
    outfile.write(elem +  '\n')

outfile.close()


