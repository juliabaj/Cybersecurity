import random
import string
import secrets


def password_generator():
    min_length = 6
    max_length = 10
    all_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password_length = random.randint(min_length, max_length)
    password_gen = ''.join(secrets.choice(all_characters) for _ in range(password_length))

    return password_gen

password_generated = password_generator()
print(password_generated)