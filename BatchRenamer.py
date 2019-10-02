#This code imports the necessary modules

import os
import re
import collections
import operator
 
print("")

rootdir = input("Please enter the directory housing the files to rename, in this fashion: 'C:\Quotes\Prime\Release': ")

print("")

filtyp = input("To change all files in the directory, please enter 'All'. To change a particular filetype, please enter the filetype suffix-- ie '.mp3' or '.jpg': ")

print("")

rootnam = input("Please enter a root string to use as the new filename basis: ")

print("")

if filtyp == "All":

    fillst = []
    fillrt = []
    filltyp = []

    for subdir, dirs, files in os.walk(rootdir):

        for file in files:
            filepath = subdir + os.sep + file
            froot = subdir + os.sep 
            fstr = str(file)
           
            nummer = fstr.rindex(".")
            
            fstr2 = fstr[nummer:]
            fillst.append(str(filepath))
            fillrt.append(str(froot))
            filltyp.append(str(fstr2))


if filtyp != "All":

    fillst = []
    fillrt = []
    filltyp = []

    for subdir, dirs, files in os.walk(rootdir):

        for file in files:
            filepath = subdir + os.sep + file
            froot = subdir + os.sep 
            if filepath.endswith(filtyp):
                fillst.append(str(filepath))
                fillrt.append(str(froot))
                filltyp.append(filtyp)

x = len(fillst)

for ctr in range(x):

    astr = fillst[ctr]
    bstr =  fillrt[ctr] + rootnam + "_" + str(ctr) + filltyp[ctr] 

    os.rename(astr, bstr) 

print("")

print("The chosen files have been renamed. Thank you.")

print("")