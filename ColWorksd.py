infile = open("Nam1.txt", "r")

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

infile = open("Mod1.txt", "r")

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

infile = open("Rec.txt", "r")

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

outlsta = []

outlstb = []

outlstc = []

outlstd = []


x = len(A2)

for ctr in range(x):
    astr = A1[ctr]
    if 'HT' in astr[:3]:
        for adder in range (1,8):
            if adder < int(A3[ctr]): 
                outlsta.append("0")
            if adder >= int(A3[ctr]):
                outlsta.append("1")
            if adder == int(A3[ctr]):
                outlstb.append("1")
            if adder != int(A3 [ctr]):
                outlstb.append("0")

    if 'HT' not in astr[:3]:

        if A3[ctr] == '1':
            outlsta.append('0')
            outlsta.append('1')
            outlsta.append('1')
            outlsta.append('1')
            outlsta.append('1')
            outlsta.append('1')
            outlsta.append('1')

            outlstb.append('1')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')

        if  A3[ctr] == '2':
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('1')
            outlsta.append('1')
            outlsta.append('1')
            outlsta.append('0')
            outlsta.append('0')

            outlstb.append('0')
            outlstb.append('1')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
        
        if  A3[ctr] =='3':
            
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
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

        if  A3[ctr] == '4':
            
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('1')
            outlsta.append('0')
            outlsta.append('0')

            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('1')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            
        if  A3[ctr] =='5':
            
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
            outlstb.append('1')
            outlstb.append('0')
            outlstb.append('0')

        if  A3[ctr] =='6':
            
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('1')

            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('1')
            outlstb.append('0')

        if  A3[ctr] =='7':
            
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')
            outlsta.append('0')

            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('0')
            outlstb.append('1')
    
    for y in range(1,8):
        z = str(y)
        outlstc.append(z)
        astr = A2[ctr]
        outlstd.append(astr)





outfile = open("scriptsa.txt", "w")

for elem in outlsta:
    outfile.write(elem +  '\n')

outfile.close()

outfile = open("scriptsb.txt", "w")

for elem in outlstb:
    outfile.write(elem +  '\n')

outfile.close()

outfile = open("scriptsc.txt", "w")

for elem in outlstc:
    outfile.write(elem +  '\n')

outfile.close()

outfile = open("scriptsd.txt", "w")

for elem in outlstd:
    outfile.write(elem +  '\n')

outfile.close()



