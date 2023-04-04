"""Functions for creating, transforming, and adding prefixes to strings."""
from string import punctuation as punc


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    word = "un" + word
    return word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    final_string = vocab_words[0] + " :: "
    for index in range(1, len(vocab_words)):
        new_word = vocab_words[0] + vocab_words[index]
        if vocab_words[index] != vocab_words[-1]:
            final_string += new_word + " :: "
        else:
            final_string += new_word
    return final_string


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word[-4:] == "ness" and word[-5] == "i":
        word = word[:-4]
        word_list = list(word)
        word_list.pop()
        word_list.append("y")
        word = "".join(word_list)

        return word
    elif word[-4:] == "ness":
        word = word[:-4]
        return word
    else:
        print("Word must end in 'ness' to be valid. Please try again.")
        return None


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set", 2) becomes "darken".
    """

    word_list = sentence.split()
    word = word_list[index]
    if word[-1] in ("a", "e", "i", "o", "u"):
        adjective = word[-1] + "n"
        return adjective
    elif word[-1] in punc:
        adjective = word.replace(word[-1], "") + "en"
        return adjective
    else:
        adjective = word + "en"
        return adjective
