fruits = ["apple","banana","cherry"] 

for x in fruits: #only valid for one dimensional
    print(x)

for x in "banana":
    print(x)

for x in fruits:
    print(x)
    if x == "banana":
        break

