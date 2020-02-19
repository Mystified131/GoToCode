infile = open("Rec.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "." or y == "-":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outlsta = []

outlstb = []


for elem in A1:
    if elem == '1':
        outlsta.append('0')
        outlsta.append('1')
        outlsta.append('0')
        outlsta.append('0')
        outlsta.append('0')
        outlsta.append('0')
        outlsta.append('0')

        outlstb.append('0')
        outlstb.append('1')
        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('0')

    if elem =='2':
        outlsta.append('0')
        outlsta.append('0')
        outlsta.append('1')
        outlsta.append('1')
        outlsta.append('1')
        outlsta.append('0')
        outlsta.append('0')

        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('1')
        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('0')
    
    if elem == '3':
        outlsta.append('0')
        outlsta.append('0')
        outlsta.append('0')
        outlsta.append('0')
        outlsta.append('0')
        outlsta.append('1')
        outlsta.append('1')


        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('0')
        outlstb.append('1')
        outlstb.append('0')


outfile = open("scriptsa.txt", "w")

for elem in outlsta:
    outfile.write(elem +  '\n')

outfile.close()

outfile = open("scriptsb.txt", "w")

for elem in outlstb:
    outfile.write(elem +  '\n')

outfile.close()