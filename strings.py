###### Adding a comment in remote repo
# Do not use reserved keywords for variable names
'''
print('Hello world')

print(help('keywords'))

# Try to avoid multiple variable declaration simultaneously
a = b = c = 10  # shortcut for below . works but not recommended
a = 10
b = 10
c = 10

print(a,b,c)

# statement vs expression
x = 47  # statement
y = x + 10  # expression

# TYPE CONVERSION --> to change the data type of the variable #
# convert floats and numeric strings to int
print(int("20"))


print(int("14.21"))
# print(int("20.24"))  # errors out because int expects only whole numbers
print(int(float("20.24")))


## STRINGS ##
# 3 ways to create a string - using either single, double, triple quotes
first_name = 'jane'
last_name = "Doe"
Address = ''10 Main St.''

job = "Physician's Assistant"  # recommended to use double qoutes for strings

## STRING FUNCTIONS

#  len() --> returns the number of characters in a string
print(len("Hello"))

# upper and lower --> convert the string to appropriate case
print("Hello".upper())

# string concatenation - adding up strings

first_name = "Jane"
last_name = "Doe"
print(first_name + ' ' + last_name)

age = 24
print(first_name + ' ' + last_name + ':' + str(age))

# string multiplication a string with an int
print("hello"*3)

# accessing string characters - a string is just a sequence of character
'''

'''
name  = "Jane Doe"
print(name[2])
# print(name[8])  # throws index out of bound error

# Retrieving the character at a given index
print(name.index('o'))  # returns 6
print(name.index('e'))  # returns the index of first occurence
'''

#### String Slicing #####

emp_name = "Jane Doe"
print(emp_name[2:6])
print(emp_name[0:4])
print(emp_name[:4])
print(emp_name[3:])
print(emp_name[-4:-1])
print(emp_name[1:6:2])  # its telling it to stay in between 1 and 6 and skip 2 characters
print(emp_name.count('e'))  # its counting how many e are in the whole name
print(emp_name.find('doe'))  # position of te sub string
print(emp_name.replace('Jane','John'))
print(emp_name)
emp_name = emp_name.replace('Jane','John')
print(emp_name)

print('oh' in emp_name) # we checked if oh is the part of the string.

## STRING FORMATING ##

Student_name = "Alex"
Score = 74

print("Name: " + Student_name + " " + str(Score))
print("Name: {} Score: {} ".format(Student_name,Score))

# f-Strings

print(f"Name: {Student_name} Score: {Score}")
print(f"3 times 10 is equal to {3*10}")



