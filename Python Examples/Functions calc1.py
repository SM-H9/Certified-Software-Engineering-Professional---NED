def sum(num1,num2):
    sum = num1 + num2
    print("The Sum is =", sum)

def diff(num1,num2):
    diff = num1 - num2
    print(f"The difference is = {diff}")

def mul(num1,num2):
    mul = num1 * num2
    print(f"The multiplication is = {mul}")

def div(num1,num2):
    div = num1 / num2
    print(f"The division is = {div}")


a = int(input("Enter a number "))
b = int(input("Enter another number "))
op = input("Enter any operator [+,-,x or /]")

if op == "+":
    sum(a,b)
elif op == "-":
    diff(a,b)
elif op == "x":
    mul(a,b)
elif op == "/":
    div(a,b)
else:
    print("You have entered an invalid operator")