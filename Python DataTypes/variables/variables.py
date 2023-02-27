# creating variables...

x = 5 
y = "mwangangi" 
print(x)
print(y)

# variables can change type in python dynamically

k =  'mwangangi'
k = 10 
print(k)

# Casting ===== If you want to specify the data type of a variable, this can be done with casting.

x = str(3)
y = int(3)
z = float(3)

print(x , y , z)

# You can get the data type of a variable with the type() function.

x = 100 
y = "python"

print(type(x))
print(type(y))

# Case-Sensitive === Variable names are case-sensitive.

a = 100 
A = "ken"

#A will not overwrite a
print(A) 

# Variable Names

# rules of variable names in python

# -its case sensitive.... A and a mean different things
# -variable name should not start with a number
# -variable name should only contain Alpha numerics character and an underscore(a-z , 0-9 and _)
# -Variable name should start with a letter or an underscore
# -Variable name should not be any of the python keywords


# Examples....
myvar = "John"
my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Multi Words Variable Names

# How to make multiwords readable

# Camel Case ==== Each word, except the first, starts with a capital letter:

myVariableName = "mwangangi"

# Pascal Case === Each word starts with a capital letter:

MyVariablename = "mwangangi"

# Snake Case === Each word is separated by an underscore character:

my_variable_name = "mwangangi"

# Python Variables - Assign Multiple Values
x,y,z = 'ken1',"onesmus","mwangangi"

# output ken1
print(x) 
# output onesmus
print(y)
# output mwangangi
print(z)

# One Value to Multiple Variables
x = y = z = "orange"

# output orange
print(x)

# output orange
print(y)

# output orange
print(z)

# Unpack a Collection === If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["mangoes" , "apples" , "bananas"]

print(fruits)
# unpack the collection...

m,a,b = fruits
# output  mangoes
print(m)

# output  apples
print(a)

# output bananas
print(b)

print(m,a,b)

# outputing multiple variables we seperate by a comma

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# we can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# Python - Global Variables

name = "mwangangi"

def calName():
    print("my name is" + name)

calName()    









