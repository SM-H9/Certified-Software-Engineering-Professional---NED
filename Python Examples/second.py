name = input("enter your name: ")
marks_phy = int (input("enter your marks in physics: "))
marks_chem = int (input("enter your marks in chemistry: "))
marks_math = int (input("enter your marks in maths: "))
total = marks_phy + marks_chem + marks_math
percentage = (total/300)*100
print(name, "your total marks are: ", total, "and your percentage is: ", round(percentage,2))
print(f"{name} your total marks are: {total} and your percentage is: {round(percentage,2)}") #same thing as above but here you do not have to add the inverted commas etc again. Only difference is that you need to add an f afer starting the print