# This is a lottery ticket generator 
import random

# I have created the userInput branch
username = input("Please enter your name: ")

# The amount of numbers the ticket must have
ticket_numbers = 6

# print random numbers
for i in range(ticket_numbers):
    print (random.randint(1,59))


