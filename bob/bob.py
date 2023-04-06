# Bob has 5 fixed responses based on the format of the hey_bob string
# Assume that the hey_bob string will be only one sentence.
# Easiest method is using regular expressions
# import re, check if hey_bob matches each regular expression and return fixed reponse based on this
# If SENTENCE ||does not match|| (regular expression), ||evaluate against|| <next> (regular expression)...
# ...until there is a match. If no match for given expressions, return "Whatever."
import re
from string import punctuation as punc


def response(hey_bob):
    # Create regular expressions that account for every edge scenario(VERY DIFFICULT!!!)
    sure = re.compile(r"[A-Z]*[a-z0-9" + re.escape(punc) + r"\s]*[?]$")
    chill_out = re.compile(
        r"^[A-Z0-9" + re.escape(punc) + r"\s]*!{0,1}[^0-9]$")
    calm_down = re.compile(r"[A-Z" + re.escape(punc) + r"\s]*[?]$")
    # Test which expression the code matches and return the corresponding statement
    # (this will break if put into a different order; needs improvement)
    if not hey_bob.strip():
        return "Fine. Be that way!"
    if sure.match(hey_bob.strip()):
        return "Sure."
    if calm_down.match(hey_bob.strip()):
        return "Calm down, I know what I'm doing!"
    if chill_out.match(hey_bob.strip()):
        return "Whoa, chill out!"
    if hey_bob[-1] == "?":
        return "Sure."
    return "Whatever."
