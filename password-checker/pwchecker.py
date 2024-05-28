def check_length(password):
    return len(password) >= 8
def check_uppercase(password):
    for char in password:
        if char == char.upper():
            return True
    return False

def check_lowercase(password):
    for char in password:
        if char == char.lower():
            return True
    return False

def check_numbers(password):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    for char in password:
        if char in numbers:
            return True
    return False

def check_special_chars(password):
    special_chars = 