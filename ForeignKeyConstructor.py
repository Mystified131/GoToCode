import datetime

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

print("")

print("Welcome to the Foreign Key Constructor.")

print("")

totable = input("What is the name of the table to which you are adding the key designation?: ")

print("")

colm = input("What is the column name in this table that will become the foreign key?: ")

print("")

datyp = input("What is the data type for the column that will become the foreign key?: ")

print("")

fromtable = input("What is the table name from which you are adding the key designation?: ")

print("")

fromcolm = input("What is the column name on this table which will become the foreign key?: ")

print("")

fromdat = input("What is the data type for this column?: ")

print("")

print("Your script will appear in the same folder as this code. Thank you.")

print("")

questr = "ALTER TABLE " + fromtable + " ALTER COLUMN " + fromcolm + " " + fromdat + " Not NULL;"

plustr = "ALTER TABLE " + totable + " ALTER COLUMN " + colm + " " + datyp + " Not NULL;"

addstr = "ALTER TABLE " + totable + " ADD FOREIGN KEY (" + colm + ") REFERENCES " + fromtable + "(" + fromcolm + ");"

afil = "FKBuilder" + tim + ".txt"

outfile = open(afil, "w")

outfile.write(questr +  '\n')
outfile.write(plustr +  '\n')
outfile.write(addstr +  '\n')
outfile.write( '\n')

outfile.close()