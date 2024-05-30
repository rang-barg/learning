import random
import string

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

def generate_password(len):
    if len < 8:
        raise ValueError("PASSWORD TOO SHORT!!!!!")
    
    total_char_set = lowercase_letters + uppercase_letters + digits + special_characters

    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    k = len - 4

    for i in range(len):
        password += random.choice(total_char_set)

    random.shuffle(password)

    return ''.join(password)

def main():
    len = int(input("Enter password length: "))
    password = generate_password(len)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()