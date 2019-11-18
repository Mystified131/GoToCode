import datetime
import os

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

rootdir = "C:\\Users\\TPark\\LocalPythonCode\\GoToCode\\Variance\\"

fillst = []

for subdir, dirs, files in os.walk(rootdir):

    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".txt"):
            fillst.append(filepath)    

print(fillst)

anslist = []

deltstra = []

filstr =  fillst[0]

infile = open(filstr, "r")

aline = infile.readline()

while aline:
    if "unique deltas were" in aline:
        bstr = aline[41: 47]
        bval = int(bstr)
        print(bval)
        deltstra.append(bval)
    aline = infile.readline()

infile.close()

deltstrb = []

filstr = fillst[1]

infile = open(filstr, "r")

aline = infile.readline()

while aline:
    if "unique deltas were" in aline:
        bstr = aline[41: 47]
        bval = int(bstr)
        deltstrb.append(bval)
        print(bval)
    aline = infile.readline()

infile.close()

print(deltstra)
print(deltstrb)

x = len(deltstra)
y = len(deltstrb)

if x >= y:

    limval = y

    for ctr in range(limval):

        ava = deltstra[ctr]
        bva = deltstrb[ctr]

        valdif = abs(ava - bva)
        valquot = 100 * (valdif / ava)
        anslist.append(valquot)
    

if y > x:

    limval = x

    for ctr in range(limval):

        ava = deltstra[ctr]
        bva = deltstrb[ctr]

        valdif = abs(ava - bva)
        valquot = 100 * (valdif / ava)
        anslist.append(valquot)
   
outstr = "Vartest_" + tim + ".txt"

outfile = open(outstr, "w")

outfile.write("Variance Test For Regression Test Round" +  '\n')

outfile.write("Compiled on " + tim + '\n')

outfile.write('\n')

outfile.write("Round marked as 'Over' indicate a higher variance than 10%, and may require investigation." + '\n')

outfile.write('\n')

x = len(anslist)

for ctr in range(x):
    if anslist[ctr] > 10:
        tval = "Over The 10% Variance Threshold"
    if anslist[ctr] < 11:
        tval = "Within The 10% Variance Threshold"
    estr = "Test " + str((ctr)+1) + ": " + str(anslist[ctr]) + "%- " + tval
    outfile.write(estr +  '\n')
    outfile.write('\n')

outfile.close()

print ("")

print ("The scripts txt file should now be available in the same folder as the python code.")   

