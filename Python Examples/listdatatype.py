list1 = [10,20,30,40,50,60,70,80,90] #the first item has an index of 0 alternatively the last item has a index of -1 so you can either go 0 onwards or go -1 onwards

print(list1)
print (type(list1))
print(list1[2])

for i in list1:
    print (i)


for i in range (len(list1)):
    print(f"List1 {i} = {list1[i]}")

for i in range (-1,-len(list1)):
    print(f"List1 {i} = {list1[i]}")


#slicing
list2 = list1[0:5] #start to 5th
print(list2)

print(list1[4:]) #4th to end

print(list1[-5:-1])