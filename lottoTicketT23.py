# This is a lottery ticket generator 
import random

# I have created the userInput branch
username = input("Please enter your name: ")

# I have created another input for the user to create a profile name
profilename = input("Please create a name for your profile: ")

# I have created the lottoCreator branch
lottoNumbers = input(int("Please enter the amount of numbers you wish to generate: "))

# The amount of numbers the ticket must have is the submitted amount from the user.
ticket_numbers = lottoNumbers

# print random numbers
for i in range(ticket_numbers):
    print (random.randint(1,59))

# I have created a feedback branch
feedback = input("Please let us know if you enjoyed this app: ")

# I have created a branch for the users email
email = input("Please enter your email address to receive our newsletter: ")
