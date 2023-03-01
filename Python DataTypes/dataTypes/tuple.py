# tuples are used to store several items in one variable

my_tuple = ("ken","mary","jane","nesh")
print((my_tuple[0]))

# tuple length

print(len(my_tuple))

single_tuple = ("mwangangi")

print((single_tuple))

tuple1 = ("abc", 34, True, 40, "male")
print((tuple1))


# changing a tuple

tuple_sample = ("orange","banana","pawpaw","glucose")
print(type(tuple_sample))

y =  list(tuple_sample)

y[1] = "mwangang"

x = tuple(y)

print((x))

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# unpacking the tuple

(a,b,c,d) = thistuple

print(a)
print(b)
print(c)
print(d)

# Using Asterisk*  ==== if the number of variables a less than the number of the values we use asterils
(a,*b,) = thistuple

print(a)
print(b)

# loping through=====

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])







