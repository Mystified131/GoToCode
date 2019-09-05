#This code imports the necessary modules

import os
import re
import datetime

def convert_file(file):
    infile = open(file, "r")

    A1 = []

    aline = infile.readline()

    bline = ""

    while aline:
        A1.append(aline)
        bline = ""
        aline = infile.readline()
    infile.close()

    return A1
    

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

newdir = "V:\\Config\\TEST\\Regression Testing\\Newer\\Regression_Testing_Results\\Results\\NewResults\\"
olddir = "V:\\Config\\TEST\\Regression Testing\\Newer\\Regression_Testing_Results\\Results\\EstablishedBaselines\\"

print("")

envir = input("What environment are the new tests from (DEV / TEST / UAT / PROD)?: ")

print("")

envir2 = input("What environment are the old, baseline tests from (DEV / TEST / UAT / PROD?: ")

print("")

dat = input("What is the later output's date, in the following form (6262019 or 7032020, etc): ")

print("")

dat2 = input("What is the date of the earlier, baseline output, in the the following form (6262019 or 7032020, etc): ")

print("")

numtest = input("How many tests are we checking today?: ")

print("")

nintest = int(numtest)

outstr = 'V:\\Config\\TEST\\Regression Testing\\Newer\\Regression_Testing_Results\\Deltareports\\Deltareport.' + envir + '.' + dat + "." + tim + '.txt'

outfile = open(outstr, "w")

for ctr in range(nintest):

    repnum = str(ctr + 1)

    fil1 = newdir + repnum + "_" + envir + "_" + dat + ".xml"
    fil2 = olddir + repnum + "_" + envir2 + "_" + dat2 + ".xml"

    outfil1 = repnum + "_" + envir + "_" + dat + ".xml"
    outfil2 = repnum + "_" + envir2 + "_" + dat2 + ".xml"

    A1 =convert_file(fil1)

    whollsta = []
    onechecka = []
    onechecka2 = []
   
    x = len(A1)
    for ctr in range(x):
        stnga = A1[ctr]
        if ('Name' in stnga) and ('Property' in stnga):
            
            a1clip = stnga.lstrip()
            inda2 = (a1clip.index('Name')-1)
            mainclipa = a1clip[1:inda2]
            whollsta.append(a1clip)
            onechecka.append(mainclipa)
 
    B1 =convert_file(fil2)

    whollstb = []
    onecheckb = []
    onecheckb2 = []

    x2 = len(B1)
    for ctr in range(x2):
        stnga = B1[ctr]
        if ('Name' in stnga) and ('</Property' in stnga):
            
            a1clip = stnga.lstrip()
            inda2 = (a1clip.index('Name')-1)
            mainclipa = a1clip[1:inda2]
            whollstb.append(a1clip)
            onecheckb.append(mainclipa)
      

    x = len(whollsta)
    x2 = len(whollstb)

    outstra = []
    outstrb = []

    for ctr in range(x):
        oca = onechecka[ctr]

        for ctr2 in range(x2):
            ocb = onecheckb[ctr2]

            if (oca in ocb):
                outstr = whollsta[ctr]
                outstra.append(outstr)
                outstr2 = whollstb[ctr2]
                outstrb.append(outstr2)

    x = len(outstra)

    deltlst = []

    anslst = []

    simct = 0

    for ctr in range(x):
        stnga = outstra[ctr]
        stngb = outstrb[ctr]
        if ('Source' in stnga) and ('Source' in stngb): 
            last1 = stnga.index('Source')
            last2 = stngb.index('Source')
            num1 = last1 + 10
            num2 = last2 + 10
            res1 = stnga[num1:]
            res2 = stngb[num2:]
            if res1 not in res2 and 'GUID' not in stnga and 'Date' not in stnga and 'QuoteFileID' not in stnga and 'Output' not in stnga and 'File' not in stnga and 'Opportunity' not in stnga and 'ProjectNumber' not in stnga and 'FolderPath' not in stnga:
                outstr = "1:" + stnga + " 2:" + stngb
                deltlst.append(outstr)
            if res1 in res2:
                simct += 1
                anslst.append(res1)


    deltotal = str(len(deltlst))

    samtot = str(simct)
  
    outfile.write('Soft Test-- Matching Property IDs to Values' +  '\n')

    outstr = "Report between " + outfil1 + " and " + outfil2

    outfile.write(outstr + '\n')

    outfile.write('\n')   

    outfile.write("The total lines with deltas were: " + deltotal +  '\n')

    outfile.write('\n')  

    outfile.write('\n')

    for elem in deltlst:

        outfile.write(elem + '\n')

        outfile.write('\n')

outfile.close()

print ("The scripts txt file should now be available in the same folder as the python code.")






