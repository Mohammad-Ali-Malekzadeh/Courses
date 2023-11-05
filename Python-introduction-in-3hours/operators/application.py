age = input("Please insert your age: ")
age = int(age)

name = input("Please insert your name: ")

if age <= 18 or name == 'Jack':
    print("Sorry, You are not allowed to enter!")
else:
    print("Welcome")