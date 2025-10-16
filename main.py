import random


def create_password(password_lenght):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(password_lenght):
        password = password + random.choice(chars)
    pass
    return password


pass_lenght = input("Choose the password lenght: ")

try:
    pass_lenght = int(pass_lenght)
    password = create_password(pass_lenght)
    print("Generated Password:", password)
except ValueError:
    print("Enter a valid number.")
