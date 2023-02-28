# Built-in Data Types

# text type =  str
# numeric types = int , float , complex
# sequence types = list , tuples , range
# mapping type = dict,
# set types =  sets , frozensets
# boolean types = bool
# binary types = bytes , bytearray , memoryview
# none type  = none

for i in range(2,20,10):
  print(i)


# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# frozensets are immutable
# fSet.add('v')

# Setting the Specific Data Type
x = str(11)
# output 11
print(x)
y = float(20.8)
# output 20.8
print(y)
print(type(y))

# complex type

comp = complex(1j)
print(comp)
print(type(comp))

l = ["evans","ken","john"]
l.insert(0,"sossy")
print((l))

# tuple datatype"
tup = tuple(("one","two","three","four"))
print(type(tup))

# range data type
print(range(0,6,2))

# dict

di = dict(name = "Mwangani" , age  = 25)
print(di)

# Python Numbers

# int
# float
# complex

# variables of numeric value are created when they assigned values

x = 10
y = 10.67
z = 3j

print(x)
print(y)
print(z)

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))



x = 35e3
y = 12E4
z = -87.7e100

print((x))
print((y))
print((z))


# Complex
# Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

# print((x))
# print(type(y))
# print(type(z))

# Type Conversion
x = 1 
y = 5.9
z = 7j

print(type(y))
int_value = int(y)
print(type(int_value))
 

#  Random Number

import random
print(random.randrange(1,10,8))

# Python Strings
