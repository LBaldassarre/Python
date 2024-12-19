import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# # SOLUTION WITH WHILE LOOP
# total_nr_of_characters = nr_letters + nr_numbers + nr_symbols

# # password characters holder
# password_list = []

# # gonna use this lists in order to generate the password randomly
# characters = [letters, numbers, symbols]
# nr_characters_left = [nr_letters, nr_numbers, nr_symbols]

# while(total_nr_of_characters > 0):
#     random_selector = random.randint(0,2)
#     if nr_characters_left[random_selector] != 0:
#         random_character = random.randint(0, len(characters[random_selector])-1)
#         password_list.append(characters[random_selector][random_character])
#         nr_characters_left[random_selector] -= 1
#         total_nr_of_characters -= 1

# password = ""
# for letter in password_list:
#     password += letter

# print(f"Your password is: {password}")

# SOLUTION WITH FOR LOOP AND SHUFFLE
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")