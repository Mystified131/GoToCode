infile = open("Mod.txt", "r")

A1 = []

aline = infile.readline()

bline = ""

while aline:
    for y in aline:
        if y.isalnum() or y == "/" or y == "-" or y == ".":
            bline+=y
    A1.append(bline)
    bline = ""
    aline = infile.readline()
infile.close()

outdic = {}

for elem in A1:
    astr = elem[:-1]
    outdic[astr] = ""

x = len(outdic)

print(outdic)

print(x)
