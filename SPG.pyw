import tkinter as tk
import secrets
import string
import random

# Check the password for duplicates
def seek_duplicates(lst):
    seen = set()
    for element in lst:
        if element in seen:
            return True
        seen.add(element)
    return False

# Check the password for duplicates, if there is one replace it with given value
def seek_and_destroy_duplicates(lst, new_value):
    seen = set()
    for i, val in enumerate(lst):
        if val in seen:
            lst[i] = new_value
            break
        else:
            seen.add(val)
    return lst

# Count the different character types of the password
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

# The main function that generates the password
def generate():
    # Generate a 20 character password base
    password_base = list(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(20))

    # Ensure user input is valid and has exactly 2 characters
    user_input = randomChars.get()
    while len(user_input) < 2:
        user_input += secrets.choice(string.ascii_letters + string.digits)

    # Add user input to password base at random position
    random_position = secrets.randbelow(len(password_base))
    password_base[random_position] = user_input[0]

    # Check for and replace duplicates
    password_base = seek_and_destroy_duplicates(password_base, user_input[1])

    while seek_duplicates(password_base):
        password_base = seek_and_destroy_duplicates(password_base, secrets.choice(
            string.ascii_letters + string.digits + string.punctuation))

    '''
    Check the number of uppercase and lowercase letters. 
    Add the less frequent letter type to the end of the password. 
    Also include a number and a special character. 
    Ensure the password is 24 characters long and make necessary adjustments.
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

        if len(password_base) > 24:
            password_base.pop()

    # The list is shuffled.
    random.shuffle(password_base)

    # Convert list to string
    generated_password = ''.join(password_base)

    # Output generated password and character counts
    generatedPass.delete("1.0", "end")
    generatedPass.insert("1.0", generated_password)

# Copy the generated password to clipboard
def copy():
    copiedText = generatedPass.get('1.0', "end")
    copiedText = copiedText[:-1]
    root.clipboard_clear()
    root.clipboard_append(copiedText)

# Console output at startup
print("Secure Password Generator v. 1.0\n2025 © Data Animal")

# Set window settings
root = tk.Tk()
root.title("Secure Password Generator")
root.geometry("370x120")
root.resizable(False, False)
root.wm_attributes('-toolwindow', 'True')

# Set widgets
randomLabel = tk.Label(root, text="Enter two random characters to strengthen the password", font=('Arial', 10))
randomChars = tk.Entry(root)
passwordLabel = tk.Label(root, text="Password: ", font=('Arial', 10))
generatedPass = tk.Text(root, width=25, height=1)
generateBtn = tk.Button(root, text="Generate", command = generate, width=10)
copyBtn = tk.Button(root, text="Copy", command = copy, width=8)

# Place widgets
randomLabel.pack()
randomChars.pack()
generateBtn.pack(pady=10)
generatedPass.pack()
passwordLabel.place(x=13, y=85)
copyBtn.place(x=295, y=84)


if __name__ == '__main__':
    root.mainloop()
