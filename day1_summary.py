type("HI44")
print(type('HI444'))

text_num = "44"
real_int = int (text_num)

print(real_int)
print(type(real_int))

num_float = float ("44.5")
num_int = int(num_float)

print(type(True))
print(type(False))

print(type(int(3.99)))

#st.format()
name = 'John'
age = 30 
print(f"My name is {name} and I am {age} years old.")

#Additional capabilities
x = 10
y = 20 
print(f"The sum of x and y is {x+y}.")
#format string inject variables into a string in python and produce mor human readable outputs
#string interpolation(f-string) , they are prfixed with 'f' and use curly braces{}

#%operator
#one of the oldest way to format strings n use %operator to replace variables in the string

name = "May"
age = 30
print('My name is % and I am % years old.')
#Raw string
regular_string = "C:\new_folder\file.txt"
print("Regular String:",regular_string)

#(\n) represents new line character
raw_string = r"C:new_folder\file.txt"
print("Raw String:", raw_string)

#What are Strings?
#Digitals and spaces in string
'1 2 3 4 5 6'
#special characters in string
'@#2]78o;47$%'
#Print the string
print("hello!")
# Assign string to variable
name = 'The BodyGuard'
name
#Indexing starts at 0, it means the first index is on the index 0.
#Print the first element in the string
print(name[0])
#negative indexing helps to count the element from the end of the string
#print the last element in the string
print(name[-1])
#find he number of the characters in the string by using len
#find the length of the string
len("The BodyGuard")

#Slicing : first no. starts from 0 and sec no. means the length from the index to the last element you want(start at 1)
#stride :
# e.g: Get every second element in therange from index 0 to index 4
name[::2]
#Concatenate two strings
#Print the string for 3 times
3 * "The BodyGuard"
# Concatenate Strings
name = 'The BodyGuard'
name = name + "is the best album"
name

#Escape Sequences: 
print("The Bodyguard\n is the best album")
#Tab escape sequence 
print("The BodyGuard \t is the best album")
#include back slack in string
print("The BodyGuard \\ is the best album")
#r will tell python that string will be displayed as raw string\
print(r"The BodyGuard \ is th best album")

#String manipulation operaations
#Convert all characters in the string to upper case
#****
a = "Thriller is the sixth studio album"
print("before upper:" , a)
b = a.upper()
print("After upper:", b)
#***
#Replace the old substring with the new target substring is the segment has been found in the string
a = "The BodyGuard is the best album"
b = a. replace ("BodyGuard", "Janet")
b
#Split the substring into list
name= "The BodyGuard"
split_string = (name.split())
split_string
#ans : ['The' , 'BodyGuard]

#RegEx is for matching and handling strings
import re
s1 = "The BodyGuard is the best album"
#Define the pattern to search for
pattern = r"Body"
#Use the search() function to search for the pattern in the string
result = re.search (pattern, s1)
#check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

pattern = r"\d\d\d\d\d\d\d\d\d\d" #Match any ten consecutive digits
text = "My phone number is1234567890" 
match = re.search ( pattern, text) 
if match:
    print("Phone number found:", match.group())
else :
    print('No Match')

pattern = r"\W" #Matches any non-word character
text = "Hello,World!"
matches = re.findall(pattern, text)
print("Matches:", matches)

#\d digit (0-9)
# \w word character (letters, numbers, underscore)
# \s space / whitespace
# Uppercase flips the rule: \W means non-word character (like commas or exclamation marks).





