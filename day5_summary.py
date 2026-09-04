#example of for loop
for i in range(0,8):
    print(i)

#use for loop to change the element in the list
squares = ["red","yellow","green","purple","blue"] 
for i in range(0,5):
    print("Before square","i", "is", squares[i])
    squares[i] = "white"
    print("After square","i","is",squares[i])

#function parameters
def greet(name):
    return "Hello, " + name
result = greet("Alice")
print(result) 


