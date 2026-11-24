import random
import string


def generate_password(length, use_symbols):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += "!@#$%^&*"

    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password


def main():
    try:
        length = int(input("Password length (min 4): "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if length < 4:
        print("Password must be at least 4 characters long.")
        return

    symbols_input = input("Include special characters? (y/n): ").strip().lower()
    use_symbols = symbols_input == "y"

    password = generate_password(length, use_symbols)
    print("Generated password:", password)


if __name__ == "__main__":
    main()