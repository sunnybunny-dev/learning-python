# Day 8: Reading and Writing Files in Python (`open()`)

## Core Concept
Python uses the built-in `open()` function to interact with external files. Using the `with` statement is the best because it automatically closes the file when done, avoiding memory leaks and file corruption.
|

##  Reading Files

### The `with` Statement

# Open and read entire file content as a single string
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#Methods for Reading Data

with open("example.txt", "r") as file:
    # 1. read(): Reads entire file (or specified number of characters)
    all_text = file.read()

    # 2. readline(): Reads a single line at a time
    first_line = file.readline()

    # 3. readlines(): Reads all lines and returns them as a list of strings
    lines_list = file.readlines()

# Iterating through lines directly (Memory efficient for large files)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes trailing newlines (\n)

##Writing & Appending Files

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("output.txt", "w") as file:
    file.write("Hello, World!\n")  # Write a single string
    file.writelines(lines)         # Write a list of strings

#Appending Data ('a')

with open("output.txt", "a") as file:
    file.write("Appended new line at the end.\n")

#Copying Files Example

# Read from source and write directly to destination
with open("source.txt", "r") as read_file:
    with open("destination.txt", "w") as write_file:
        for line in read_file:
            write_file.write(line)

