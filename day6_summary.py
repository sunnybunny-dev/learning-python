#Try except
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a =a/b
    print("Success a=",a)
except:
    print("There was an error")

#Try Except /except else/finally Specific Exampke
a=1
try:
    b = int(input("Please enter a number to divide"))
    a = a/b
    print("Success a=", a)
except ZeroDivisionError:
    print("The number you provided can't divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing complete")

#Practice

import math
def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Plese enter a positve integer or a float value.")

#Handling Generic exceptions

def complex_calculation(num):
    try:
        result = num / (num-5)
        print(f"Result: {result}")
    except Exception as e:
        print("An error occurred during calculation.")

#e.g:
class Car:
    #Class attribute (shared by all instances)
    max_spped = 120 #max spped in km/h
    #constructor method 
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model= model
        self.color= color
        self.speed=speed #intial spped sets to 0

class Book(object):
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is not available.")

    def return_book(self):
        self.copies_available += 1
        print(f"You returned '{self.title}'.")  

class Circle:
    def __init__(self, radius, color):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
        self.color = color

try:
    user_radius = float(input("Enter the radius of the circle: "))
    circle = Circle(user_radius, "red")
except ValueError as e:
    print("Error:", e)
else:
    print(f"Created a {circle.color} circle with radius {circle.radius}")  