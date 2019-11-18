infile = open("IDs.txt", "r")

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


outlst = []

for elem in A1:
    astr = "Delete from dbo.KitPartPricing_Pricing where KitPartNumber = '" + elem + "' and KitPartDescr LIKE '%' + ' SL';"
    outlst.append(astr)


outfile = open("scriptsb.txt", "w")

for elem in outlst:
    outfile.write(elem +  '\n')

outfile.close()


