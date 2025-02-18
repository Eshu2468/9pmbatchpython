'''
in python, Input() function is used to take user input from the console
when input fuctions are called in python, it waits for the user to type something
and once user press enter after typing , it returns the entered data as a string
'''

user_input=input("Enter something:")
print(user_input)
print(type(user_input))

# example2

name = input("what's your name?")
print("Hello,"+ name + "!") 

# example3

age=int(input("enter your age:"))
print("you are" , age ,"years old.")

# example4

first_name = input("enter your first name:")
last_name= input("enter your last name:")
print("Hello," + first_name + " " + last_name )

