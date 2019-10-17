import datetime

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

print("")

numt = input("How many tests are we checking variance on today, please?: ")
print("")
num = int(numt)

anslist = []

for x in range(num):
    aval = input("What is the total unique deltas value for test " + str((x)+1) + ", earlier iteration?: ")
    print("")
    ava = int(aval)
    bval = input("What is the total unique deltas value for test " + str((x)+1) + ", later iteration?: ")
    print("")
    bva = int(bval)
    valdif = abs(ava - bva)
    valquot = 100 * (valdif / ava)
    anslist.append(valquot)

outstr = "Vartest_" + tim + ".txt"

outfile = open(outstr, "w")

outfile.write("Variance Test For Regression Test Round" +  '\n')

outfile.write("Compiled on " + tim + '\n')

outfile.write('\n')

outfile.write("Rounds marked as 'Over' indicate a higher variance than 10%, and may require investigation." + '\n')

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

