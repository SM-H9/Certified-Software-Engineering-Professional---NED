num1 = int(input("Enter any number"))

factorial = 1

for i in range(num1,1,-1):
    factorial = factorial*i

print(f"factorial of {num1} is {factorial}")
