# Python Cheat Sheet: Conditions, Comparison Operators, and Loops

## Conditions and Branching
Used to make decisions in code.

if condition:
    # code to execute if condition is True
elif another_condition:
    # code if another_condition is True
else:
    # code if none of the above conditions are True
Indentation is crucial to define blocks.

Comparison Operators (produce Boolean values)

Operator	Description	Example	Result
==	Equal to	5 == 5	True
!=	Not equal to	5 != 3	True
<	Less than	3 < 5	True
>	Greater than	5 > 3	True
<=	Less than or equal to	3 <= 3	True
>=	Greater than or equal to	5 >= 4	True
Loops

For Loop

Repeats code for each item in a sequence.

for variable in sequence:
    # code to execute
Example:

for color in ["red", "green", "blue"]:
    print(color)
Range Function

Generates a sequence of numbers.

range(stop) generates from 0 to stop-1.
range(start, stop) generates from start to stop-1.
Example:

for i in range(1, 6):
    print(i)
Enumerate Function

Provides index and value when looping.

Example:

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
While Loop

Repeats code while a condition is True.

while condition:
    # code to execute
Example:

count = 1
while count <= 5:
    print(count)
    count += 1

