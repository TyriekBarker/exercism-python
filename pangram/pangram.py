# Test if sentence has all the words in the english language

# Real world considerations:
# What is the max length a sentence can be?
# What are the allowed characters in a sentence?
# How would you program this to check for multiple occurances of the same letter?
# How would one standardize this program for different languages?
# How would one increase efficiency using external libraries?
# What commercial products could this or similar programs be integrated into?

from string import ascii_lowercase


def is_pangram(sentence):
    alphabet = ascii_lowercase
    # iterate through sentence formatted to be lowercase
    for letter in sentence.lower():
        # remove letter from alphabet string if it is unique
        if letter in alphabet:
            alphabet = alphabet.replace(letter, "")
        else:
            continue
    # check if alphabet string is empty using bool statement; if so, return true
    if not alphabet:
        return True
    # return false by default
    return False
