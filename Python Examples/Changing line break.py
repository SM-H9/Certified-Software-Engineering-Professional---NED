#end="" allows you to stop breaking the line and brings text to one line

for i in range (1,10):
    print("*", end ="") #no space
print("") #new line
for i in range (1,10):
    print("*", end =" ") #space
print("")
for i in range (1,10):
    print("*", end = "@") #using a custom character instead of space
print("")