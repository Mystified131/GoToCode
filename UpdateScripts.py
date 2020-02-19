#This code defines a list of bat files to edit

filenames = ["Deploy_Prod", "Profile_Update", "shortcutBuilder", "Copy_AdditionalDLLs_PROD"]

#This code dubs in the new values and saves them

for flnm in filenames:

    outstr = "NEW_" + flnm + ".bat"

    infile = open(flnm + ".bat", "r")
    outfile = open(outstr, "w")

    content = []

    aline = infile.readline()

    while aline:
        content.append(aline)
        aline = infile.readline()
    infile.close()

    contentnew = []

    for element in content:
        elem2 = element.replace("8.16.4", "8.17.1")
        contentnew.append(elem2)

    for elem in contentnew:
         outfile.write(elem)

    outfile.close()