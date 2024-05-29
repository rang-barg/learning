def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return any(char.isupper() for char in password)

def check_lowercase(password):
    return any(char.islower() for char in password)

def check_numbers(password):
    return any(char.isdigit() for char in password)

def check_special_chars(password):
    special_chars = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','\\','|',':',';',',','.','<','>','/','?','\'','"','`','~']
    return any(char in special_chars for char in password)

def evaluate_password(password):
    checks = [
        ("Length", check_length(password)),
        ("Uppercase Letters", check_uppercase(password)),
        ("Lowercase Letters", check_lowercase(password)),
        ("Numbers", check_numbers(password)),
        ("Special Characters", check_special_chars(password))
    ]

    score = sum(check for _, check in checks)

    if score == len(checks):
        strength = "Strong"
    elif score >= len(checks) // 2:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    feedback = [criterion for criterion, passed in checks if not passed]

    return strength, feedback, score

def main():
    password = input("Enter your password: ")
    strength, feedback, score = evaluate_password(password)
    print(f"Password Strength: {strength}")
    if feedback:
        print("Improve password by addressing the following:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()