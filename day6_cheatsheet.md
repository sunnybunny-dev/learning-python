# Day 6 Cheat Sheet: Exception Handling & OOP

## 1. Exception Handling
Used to handle errors gracefully without crashing your program.

```python
try:
    getfile = open("file.txt", "r")
    getfile.write("My file for exception handling.")
except IOError:
    print("Unable to open or read the data in the file.")
except Exception as e:
    print(f"Some other error occurred: {e}")

bjects and Classes
Creating Objects
Instantiation using class constructors.
obj = ClassName(value1, value2)

Accessing Attributes and Methods
Use dot notation:

obj.attribute1
obj.method_name(args)

Modifying Attributes

obj.attribute1 = new_value

Useful Built-in Functions
type(obj): Returns the class type of the object.

dir(obj): Lists all attributes and methods associated with the object.

