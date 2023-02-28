# boleans  --->represents true or false
print(10 > 9)
print(10 == 9)
print(10 < 9)

# evaluate values

print(bool("hello"))
print(bool(10))

x = "Hello"
y = 15

print(bool(x))


# values that evaluates to false

print(bool(False))
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# an object can return false is is derived from a class that returns a 0

class myclass():
  def __len__(self):
    return 0

myobj = myclass()

print("hello....")
print(bool(myobj))

# functions can return true or false....
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int))

# 
print((6 + 3) - (6 + 3))
