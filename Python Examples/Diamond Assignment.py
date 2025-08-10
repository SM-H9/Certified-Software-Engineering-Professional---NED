size = 5 
#upper half
for i in range (1, size + 1):
    print (" " * (size-i),end="")
    for j in range (i):
        print ("* ",end="")
    print()

#lower half
for i in range (size,0,-1):
    print(" "*(size-i),end="")
    for j in range (i):
        print("* ",end="")
    print()