# Python Lists
mylist = ["apple", "banana", "cherry"]
print(mylist)

# list item are changeble , ordered , 

# allow duplicate  === items in a list are indexed so they can allow duplicate values


thislist = ("apple", "banana", "cherry", "apple", "cherry")

print(thislist)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]

for i in range(len(thislist)):
  print(thislist[i])

print(thislist.__len__())


# List Comprehension offers the shortest syntax for looping through lists:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# sorting list 

thislist = ["orange", "mango", "ANN" ,"kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)





  


