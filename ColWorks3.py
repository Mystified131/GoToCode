infile = open("1a.txt", "r")

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

infile = open("1b.txt", "r")

A2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    A2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

EvDic = {}

x = len(A1)

for ctr in range(x):
    EvDic[A2[ctr]] = A1[ctr]

infile = open("2a.txt", "r")

A3 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    A3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("2b.txt", "r")

A4 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    if bline.startswith("L"):        
        cline = bline[:5] + " " + bline[4:]
        A4.append(cline)
    if not bline.startswith("L"): 
        A4.append(bline) 
    
    bline = ""
    aline = infile.readline()
infile.close()


x = len(A3)

for ctr in range(x):
    EvDic[A4[ctr]] = A3[ctr]

infile = open("3a.txt", "r")

A5 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    A5.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("3b.txt", "r")

A6 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-":
            bline+=y
    cline = bline[:2] + bline[4:-1]
    A6.append(cline)
    bline = ""
    aline = infile.readline()
infile.close()


x = len(A1)

for ctr in range(x):
    EvDic[A6[ctr]] = A5[ctr]

print(EvDic)

infile = open("TotMod3.txt", "r")

A7 = []
A8 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " ":
            bline+=y
    if bline.startswith("L"):
        cline = bline[:4] + " " + bline[4:]
        A7.append(cline)
    #if bline.startswith("L") and len(bline) < 11:
        #cline = bline[:3] + " " + bline[5:]
        #A7.append(cline)
    if bline.startswith("C"):
        cline = bline[:2] + bline[4:9]
        A7.append(cline)
    if not bline.startswith("L") and not bline.startswith("C"):
        A7.append(bline)
    A8.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outfile = open("scriptsout1.txt", "w")

for elem in EvDic:
    outfile.write(elem +  '\n')

outfile.close()

outfile = open("scriptsout2.txt", "w")

for elem in EvDic:
    astr = EvDic[elem]
    outfile.write(astr +  '\n')

outfile.close()

infile = open("KMod.txt", "r")

KM = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == " " or y == "-":
            bline+=y
    if bline.startswith("C"):
        cline = bline[:-1]
        KM.append(cline)
    if not bline.startswith("C"):
        KM.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

infile = open("k1.txt", "r")

K1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " " or y == ":" or y == "." or y == "%" :
            bline+=y
    K1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

OneDic = {}

x = len(KM)

for ctr in range(x):
    OneDic[KM[ctr]] = K1[ctr]

infile = open("k2.txt", "r")

K2 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " "  or y == ":" or y == "." or y == "%"  :
            bline+=y
    K2.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

TwoDic = {}

x = len(KM)

for ctr in range(x):
    TwoDic[KM[ctr]] = K2[ctr]

print(TwoDic)

infile = open("k3.txt", "r")

K3 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " "  or y == ":" or y == "." or y == "%" :
            bline+=y
    K3.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

ThreeDic = {}

x = len(KM)

for ctr in range(x):
    ThreeDic[KM[ctr]] = K3[ctr]

infile = open("k4.txt", "r")

K4 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " " or y == ":" or y == "." or y == "%"  :
            bline+=y
    K4.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

FourDic = {}

x = len(KM)

for ctr in range(x):
    FourDic[KM[ctr]] = K4[ctr]

infile = open("k5.txt", "r")

K5 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " "  or y == ":" or y == "." or y == "%" :
            bline+=y
    K5.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

FiveDic = {}

x = len(KM)

for ctr in range(x):
    FiveDic[KM[ctr]] = K5[ctr]

infile = open("k6.txt", "r")

K6 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " "  or y == ":" or y == "."or y == "%"  :
            bline+=y
    K6.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

SixDic = {}

x = len(KM)

for ctr in range(x):
    SixDic[KM[ctr]] = K6[ctr]

infile = open("k7.txt", "r")

K7 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " " or y == ":" or y == "." or y == "%"  :
            bline+=y
    K7.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

SevenDic = {}

x = len(KM)

for ctr in range(x):
    SevenDic[KM[ctr]] = K7[ctr]

infile = open("k8.txt", "r")

K8 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " "  or y == ":" or y == "."or y == "%"  :
            bline+=y
    K8.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

EightDic = {}

x = len(KM)

for ctr in range(x):
    EightDic[KM[ctr]] = K8[ctr]

infile = open("k9.txt", "r")

K9 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " "  or y == ":" or y == "." or y == "%" :
            bline+=y
    K9.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

NineDic = {}

x = len(KM)

for ctr in range(x):
    NineDic[KM[ctr]] = K9[ctr]

infile = open("k10.txt", "r")

K10 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " "  or y == ":" or y == "." or y == "%" :
            bline+=y
    K10.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

TenDic = {}

x = len(KM)

for ctr in range(x):
    TenDic[KM[ctr]] = K10[ctr]

infile = open("k11.txt", "r")

K11 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == " "  or y == ":" or y == "."or y == "%"  :
            bline+=y
    K11.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

ElevenDic = {}

x = len(KM)

for ctr in range(x):
    ElevenDic[KM[ctr]] = K11[ctr]

outfile = open("scripts1.txt", "w")

for elem in A7:
    if elem in OneDic:
        astr = OneDic[elem]
    if not elem in OneDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts2.txt", "w")

for elem in A7:
    if elem in TwoDic:
        astr = TwoDic[elem]
    if not elem in TwoDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts3.txt", "w")

for elem in A7:
    if elem in ThreeDic:
        astr = ThreeDic[elem]
    if not elem in ThreeDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts4.txt", "w")

for elem in A7:
    if elem in FourDic:
        astr = FourDic[elem]
    if not elem in FourDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts5.txt", "w")

for elem in A7:
    if elem in FiveDic:
        astr = FiveDic[elem]
    if not elem in FiveDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts6.txt", "w")

for elem in A7:
    if elem in SixDic:
        astr = SixDic[elem]
    if not elem in SixDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts7.txt", "w")

for elem in A7:
    if elem in SevenDic:
        astr = SevenDic[elem]
    if not elem in SevenDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts8.txt", "w")

for elem in A7:
    if elem in EightDic:
        astr = EightDic[elem]
    if not elem in EightDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts9.txt", "w")

for elem in A7:
    if elem in NineDic:
        astr = NineDic[elem]
    if not elem in NineDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts10.txt", "w")

for elem in A7:
    if elem in TenDic:
        astr = TenDic[elem]
    if not elem in TenDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scripts11.txt", "w")

for elem in A7:
    if elem in ElevenDic:
        astr = ElevenDic[elem]
    if not elem in ElevenDic:
        astr = 'NULL'
    outfile.write(astr +  '\n')

outfile.close()

outfile = open("scriptsmod.txt", "w")

for elem in A7:

    outfile.write(elem +  '\n')

outfile.close()

print(A7)

