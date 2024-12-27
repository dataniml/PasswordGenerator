import secrets
import string
import random
import math
from datetime import datetime

# A function that seeks duplicates from the generated password base
def seek_duplicates(list):
  seen = set()
  for element in list:
    if element in seen:
      return True
    seen.add(element)
  return False

# A function that seeks duplicates and replaces the first (and only the first) one with given new value
def seek_and_destroy_duplicates(list, new_value):
    seen = set()
    for i, val in enumerate(list):
        if val in seen:
            list[i] = new_value
            break
        else:
            seen.add(val)
    return list

# A function that counts the number of letters, numbers and special characters in a password
def count_types(list):
  characters = 0
  numbers = 0
  specials = 0
  for i in ''.join(list):
    if i.isalpha():
      characters += 1
    elif i.isdigit():
      numbers += 1
    else:
      specials += 1
  return {'Letters': characters, 'Numbers': numbers, 'Special characters': specials}

# Choose random number between 21-23. This will be the digit that is chosen from the datetime string
randomNumber = random.randint(21,23)

# Current datetime will be saved to variable date
date = str(datetime.now())

# From the string "date" we extract two numbers, one between 21-23 and the last one
randomizedNumberOne = date[randomNumber]
randomizedNumberTwo = date[len(date)-1]

# We'll ask user input for generating the rest of the seed
userInput = input("Give two random characters: ")

# If the input is less than 2 characters we will add random characters ourself
if len(userInput) < 2:
    helpCharacters = string.ascii_letters + string.digits
    addition = ''.join(random.choice(helpCharacters) for i in range(2))
    userInput = userInput + addition


# Let's create the 19 character password base
passwordBase = list(''.join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(19))))

# User input will be added to the created password base, first character at the place of addition of two generated random numbers
# Max value for randomizedNumberThree is (9+9=) 18, so it will never be outside the list.
randomizedNumberThree = int(randomizedNumberOne) + int(randomizedNumberTwo)
passwordBase[randomizedNumberThree] = userInput[0]

# Let's check the password base for duplicates, if we find one we will replace it with the user input
passwordBase = seek_and_destroy_duplicates(passwordBase, userInput[1])

# Another round of duplicate search. This time we'll replace a possible duplicate with a random character
if seek_duplicates(passwordBase):
    passwordBase = seek_and_destroy_duplicates(passwordBase, random.choice(string.ascii_letters + string.digits + string.punctuation))

# Let's reverse the list and check it for the duplicates for one last time
passwordBase.reverse()
if seek_duplicates(passwordBase):
    passwordBase = seek_and_destroy_duplicates(passwordBase, random.choice(string.ascii_letters + string.digits + string.punctuation))

# Converting the list back to string
generatedPassword = ''.join(passwordBase)

# Generated password
print("Password: " + generatedPassword)
print(count_types(passwordBase))
