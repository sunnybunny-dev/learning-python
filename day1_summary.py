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