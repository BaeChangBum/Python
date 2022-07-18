import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your Password?\n"))
nr_symbols = int(input("How many symbols would you like in your Password?\n"))
nr_numbers = int(input("How many numbers would you like in your Password?\n"))

total_pass = list()
total_password = ""

for i in range(0, nr_letters):
    total_pass.append(random.choice(letters))

for n in range(0, nr_symbols):
    total_pass.append(random.choice(symbols))

for k in range(0, nr_numbers):
    total_pass.append(random.choice(numbers))

random.shuffle(total_pass)

print(total_pass)

for n in range(0, len(total_pass)):
    total_password += total_pass[n]


print(total_password)