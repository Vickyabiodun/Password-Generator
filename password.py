#Password Generator Project
"""First I imported the random module"""
import random

"""These are the variables we will be selecting from at random"""
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

"""These section has variables which will receive input from users"""
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

"""I created an empty list where the random selection will be appended to"""
password = []

"""A for loop to loop through the letter, numbers and symbols variable"""
for characters in range(1, nr_letters + 1):
    password.append(random.choice(letters))
for characters in range(1, nr_symbols + 1):

    password.append(random.choice(symbols))

for characters in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))

"""This shuffles the content of the password and mixes the three variable's content together"""
random.shuffle(password)

"""Converting the list to a string"""
string_password = ''
for letter in password:
    string_password += letter
print(string_password)

