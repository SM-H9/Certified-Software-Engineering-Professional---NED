num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
opr = input("Enter the operator: ")

if opr == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif opr == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif opr == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif opr == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
else:
    print("Invalid Operator")