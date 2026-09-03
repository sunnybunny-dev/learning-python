#Using if,elif, and else atatements for a program for concert entry based on age using branching

age= int(input("Enter your age: "))
if age >= 19:
    print("You can enter the AC/DC concert.")
elif age == 18:
    print("You can go see Pink Floyd concert.")
else:
    print("You cannot enterthe AC/DC concert, but you can attend the Meatloaf concert.")

#Equality operator
age = 25
if age == 25:
    print("You are 25 years old.")

#Inequality operator
if age != 30:
    print("You are not 25 years old.")

#Greater than and less than
if age >= 20:
    print("Yes, the age is greater than 20.")

#Branching  #The if statement
age = 20
if age >= 21:
    print("You can enter the bar.")
else:
    print("Sorry, you cannot enter the bar,")

#the elif statement
if age >= 21:
    print("You can enter the bar.")
elif age >= 18:
    print("You can watch a movie.")
else:
    print("Sorry,you cannot do either")

#Real-life example:ATM 

user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = int(input("Enter the amount to withdraw: "))
    if amount % 10 == 0 :
        print("Amount dispensed: ", amount)
    else:
        print("Please enter a multiple od 10.")
else:
    print("Thank you for using the ATM.")

#Logical operators #Real-life example : Notification setting

is_do_not_distrub = True
if not is_do_not_distrub:
    send_notification("New message received") # type: ignore

#The AND operator #real life example:Access control

has_valid_id_card = True
has_matching_fingerprint = True
if has_valid_id_card and has_matching_fingerprint:
    open_high_security_door() # pyright: ignore[reportUndefinedVariable]



