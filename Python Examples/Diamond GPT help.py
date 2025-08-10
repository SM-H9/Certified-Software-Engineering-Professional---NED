#Help fro  GPT
size = 5

size = 5

# Upper half
for i in range(1, size + 1):
    print(" " * (size - i), end="")  # leading spaces
    for j in range(i):
        print("* ", end="")          # star with trailing space
    print()

# Upper half
for i in range(1, size + 1):
    print(" " * (size - i), end="")  # leading spaces
    for j in range(i):
        print("* ",end="")
    print()
    