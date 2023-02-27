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

