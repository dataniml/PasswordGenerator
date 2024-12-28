import secrets
import string
import random

def seek_duplicates(lst):
    seen = set()
    for element in lst:
        if element in seen:
            return True
        seen.add(element)
    return False

def seek_and_destroy_duplicates(lst, new_value):
    seen = set()
    for i, val in enumerate(lst):
        if val in seen:
            lst[i] = new_value
            break
        else:
            seen.add(val)
    return lst

def count_types(lst):
    characters = {'uppercase': 0, 'lowercase': 0}
    numbers = 0
    specials = 0
    for i in ''.join(lst):
        if i.isalpha():
            if i.isupper():
                characters['uppercase'] += 1
            else:
                characters['lowercase'] += 1
        elif i.isdigit():
            numbers += 1
        else:
            specials += 1
    return {'Capitalized letters': characters['uppercase'],
            'Small letters': characters['lowercase'],
            'Numbers': numbers,
            'Special characters': specials}

# Generate a 20 character password base
password_base = list(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(20))

# Ask user input for two random characters
user_input = input("Give two random characters: ")

# Ensure user input is valid and has exactly 2 characters
while len(user_input) < 2:
    user_input += secrets.choice(string.ascii_letters + string.digits)

# Add user input to password base at random position
random_position = secrets.randbelow(len(password_base))
password_base[random_position] = user_input[0]

# Check for and replace duplicates
password_base = seek_and_destroy_duplicates(password_base, user_input[1])

while seek_duplicates(password_base):
    password_base = seek_and_destroy_duplicates(password_base, secrets.choice(string.ascii_letters + string.digits + string.punctuation))

'''
Checks the number of uppercase and lowercase letters. 
Adds the less frequent letter type to the end of the password. 
Also includes a number and a special character. 
Ensures the password is 24 characters long and makes necessary adjustments.
'''
while len(password_base) < 24:
    amountOfTypes = count_types(password_base)
    if amountOfTypes['Capitalized letters'] < amountOfTypes['Small letters']:
        additionLetter = secrets.choice(string.ascii_letters).upper()
    else:
        additionLetter = secrets.choice(string.ascii_letters).lower()

    password_base.append(additionLetter)

    if amountOfTypes['Numbers'] < 5:
        additionNumber = secrets.choice(string.digits)
        password_base.append(additionNumber)

    if amountOfTypes['Special characters'] < 5:
        additionSpecial = secrets.choice(string.punctuation)
        password_base.append(additionSpecial)

# The list is shuffled.
random.shuffle(password_base)

# Convert list to string
generated_password = ''.join(password_base)

# Output generated password and character counts
print("Password: " + generated_password)
print(count_types(password_base))