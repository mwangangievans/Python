# Multiline Strings === You can assign a multiline string to a variable by using three quotes:

text = """hello python development,python is easy and effective for web development,
ready to learn new concepts everyday"""

print(text)


# Strings are Arrays

# strings in python are arrays representented in unicode.

a = "hello mwangangi"
print(a[6])

# Looping Through a String

_text = "hello jambo kenya"

for i in _text:
    print(i)

# String Length
# to get string lenth we use len() function

string_length = "hakuna matata"

print(len(string_length))
print("second method to get length", string_length.__len__())

# Check String === To check if a certain phrase or character is present in a string, we can use the keyword in.

_marion =  "marion is a medical student"
print("student" in _marion)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'frees' is present.")

#   Check if NOT  === To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)



        
