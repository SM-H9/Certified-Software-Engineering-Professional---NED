#integer int eg:
i =10

# float eg:
j=4.5

#string eg:
k = 'example' # you can either use '' or "" but be consistent

#boolean bool
b = True
f = False 

#list: this is an unordered data type and is changeable meaning we can add or subtract values from it using append and remove
list1 = ['ali','hadi','amo']
print(list1)
list1.append('muneeb')
print(list1)
list1.remove('ali')
print(list1)

#Tuple: This is an unchangeable datatype eg:
dob = ('1965', 2, 12)
print (dob, type(dob))

#Set: this is a unique type
courses = {'Python','Jave','C#'}
print (courses)
#if in the above I add python again then it wont give an error but during print or count it would count it as one only eg
courses = {'Python','Jave','C#','Python'}
print (courses)
#union and intersection in Set
first_sem_courses = {'Python','Jave','C#'}
second_sem_courses = {'AI','Deep Learning','Machine Learning','Python'}

all_sem_courses = first_sem_courses.union(second_sem_courses)
print(all_sem_courses)
common_sem_courses = first_sem_courses.intersection(second_sem_courses)
print(common_sem_courses)
#to add values to set we can use add 

print('all_sem_courses.add('abc')')