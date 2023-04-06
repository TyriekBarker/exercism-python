# Bob has 5 fixed responses based on the format of the hey_bob string
# Assume that the hey_bob string will be only one sentence.
# Easiest method is using regular expressions

# import re, check if hey_bob matches each regular expression and return fixed reponse based on this
# If SENTENCE ||does not match|| (regular expression), evaluate against next (regular expression)...
# ...until there is a match. If no match for given expressions, return "Whatever."
# ALWAYS have a thorough understanding of the end result before writing your code
import re


def response(hey_bob):
    sure = re.compile("[A-Za-z\"-// q ]*[?]$")

    chill_out = re.compile("^[A-Z\"-// ]+$")
    print(chill_out.match(hey_bob))
    calm_down = re.compile("[A-Z\"-// ]*[?]$")

    if not hey_bob.strip():
        return "Fine, be that way!"
    elif sure.match(hey_bob):
        return "Sure."
    elif chill_out.match(hey_bob):
        return "Whoa, chill out!"
    elif calm_down.match(hey_bob):
        return "Calm down, I know what I'm doing!"
    else:
        return "Whatever."
