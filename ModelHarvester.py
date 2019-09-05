#This code imports the necessary modules

import os
import re
import datetime
import collections
import operator
 
right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

rootdir = "V:\Quotes\Prod\Release"

modlst = []

datlst = []

for subdir, dirs, files in os.walk(rootdir):

    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith("00.Quote.00.xml"):
            print(filepath)
            infile = open(filepath, "r")

            aline = infile.readline()

            bline = ""

            cline = ""
          
            while aline:

                if "<Department>" in aline and "</Department>" in aline: 
                    lloc = aline.index("<Department>") + 12
                    rloc = aline.index("</Department>")

                    bline = aline[lloc: rloc]

                if "<Quote created" in aline: 
                    lloc = aline.index("<Quote created") + 16
                    rloc = aline.index("<Quote created") + 27

                    cline = aline[lloc: rloc]

                  

                aline = infile.readline()


            if bline:
                print(bline)  
                print(cline)
                modlst.append(bline)
                datlst.append(cline)

            
            infile.close()

outlst = {}

for elem in modlst:
    if elem in outlst.keys():
        outlst[elem] += 1
    if elem not in outlst.keys():
        outlst[elem] = 1

outlist = []

for elem in outlst:
    instr = ""
    if outlst[elem] < 10:
        instr = "00" + str(outlst[elem])
    if outlst[elem] > 9 and outlst[elem] < 100:
        instr = "0" + str(outlst[elem])
    if outlst[elem] > 99:
        instr = str(outlst[elem])
    astr = instr + ": " + elem
    outlist.append(astr)  

outlist.sort(reverse = True)

combolst = []

x = len(modlst)

for ctr in range(x):
    endstr = modlst[ctr] + ": " + datlst[ctr]
    combolst.append(endstr)

outstr = 'ModelReport '  + tim + '.txt'

outfile = open(outstr, "w")

outfile.write("Model Report For Quotes In PROD On: " + tim + '\n')

outfile.write("" + '\n')

outfile.write("Each sold unit and the number of sales:" '\n')

outfile.write("" + '\n')

for elem in outlist:
    outfile.write(elem +  '\n')

outfile.write("Each sold unit and the date of each sale:" '\n')

outfile.write("" + '\n')

for elem in combolst:
    outfile.write(elem +  '\n')

outfile.close()

print ("The Model Report txt file should now be available in the same folder as the python code.")






