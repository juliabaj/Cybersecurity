import re

def is_valid(password):
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d', password):      #at least one digit
        return False

    if not re.search(r'[!@#$%^&8(),.?:{}]', password):
        return False

    return True

password = input("Input your password: ")
check = is_valid(password)

if check:
    print("Valid password: ")
else:
    print("Not valid.")
