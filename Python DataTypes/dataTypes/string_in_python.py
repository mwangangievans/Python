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

_marion = "marion is a medical student"
print("student" in _marion)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'frees' is present.")

#   Check if NOT  === To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)

# Python - Slicing Strings

# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

_muthomi = "muthomi  likes c#"

print(_muthomi[2:5])

# Slice From the Start
print(_muthomi[:5])

# Slice To the End
print(_muthomi[3:])

# Python - Modify Strings

print(_muthomi.upper())

# lower case

print(_muthomi.lower())


# Remove Whitespace === its the space before and after a string

_evans = "   hello mwangangi  "

print(_evans)
print(_evans.strip())

# Replace String  === replace() method replaces a string with another

_john = "python is the best...."
# print(_john)

print(_john.replace("python", "javascript"))

# print(_john)

a = "Hello, World!"
print(a.replace("H", "J"))

_dummy_paragraph = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."


print(_dummy_paragraph.replace("Lorem" , "mwangangi"))


# Split String === The split() method returns a list where the text between the specified separator becomes the list items.

# The split() method splits the string into substrings if it finds instances of the separator:

_hello = "Loren Mwan , gangi"

print(_dummy_paragraph.split(" "))

# Python - String Concatenation

a = "Evans"

b = "mwangangi"

print(a + " "+ b)

# Python - Format - Strings

#  we can combine strings and numbers by using the format() method!



age = 36
name = "mwangangi"
txt = "My {} is John, I am  {}"
print(txt.format(age,age))

_country = "kenya"
_item = "phone"
_quantity = "2"
_sentence = "i bought {1} {2} at $200 in {0}"

print(_sentence.format(_country,_quantity,_item))
