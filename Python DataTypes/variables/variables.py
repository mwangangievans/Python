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




