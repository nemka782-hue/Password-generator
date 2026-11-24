import random
import string


def generate_password(length):
    chars = string.ascii_letters + string.digits
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password


length = int(input("Password length: "))
print("Generated password:", generate_password(length))