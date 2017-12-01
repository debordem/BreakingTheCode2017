###############################################
# LetterToNumber.py
# Vandenburg 2015 / De Borde 2017
##############################################

# INSTRUCTIONS

##############################################################
# Your task is to write a program in Python that:
# 1) Asks the user to type in a letter
# 2) Finds the position of that letter in the alphabet
# 3) Display that letter back to the user
##############################################################


# Create a variable with all the letters in the alphabet
alphabet="abcdefghijklmnopqrstuvwxyz"

# Ask the user to type in a letter
word=input("Please type a word: ")

# Ask the user to type in key
key=input("Please type a key: ")

print("The word is %s" % word)
# Find the position of the letter in the alphabet
#pos=alphabet.find(letter)


for letter in word:

    # TEST IF UPPERCASE
    if letter.isupper():
        print("upper case")
        letter = letter.lower()

    pos=alphabet.find(letter)

    # As the first position is 0, we need to add 1
    pos += 1

    #display the number back to the user
    print(pos)

    #encode
    pos = pos - int(key)

    print("new pos = %s" % pos)

    print("new letter = %s" % alphabet[pos])
