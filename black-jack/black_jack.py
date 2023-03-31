"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
from typing import Union
import json


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # Check if a jack, queen or king was passed and return 10 for either
    if card == 'J' or card == 'Q' or card == 'K':
        return 10
    # Check if an ace was passed and return 1
    elif card == 'A':
        return 1
    # Check if a valid numerical value was passed
    elif int(card) in range(2, 11):
        return int(card)

    # If not valid string passed, value is null
    else:
        print("Invalid input. No value will be returned.")
        return None


def higher_card(card_one: str, card_two: str) -> Union[int, tuple]:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # PREP
    # Write conditional to see which card has higher value
    # Return card with higher value
    # If same value, return tuple with both cards

    # Check that both cards are valid before running conditionals
    if value_of_card(card_one) and value_of_card(card_two):

        # Check which card has higher value
        if value_of_card(card_one) > value_of_card(card_two):
            return card_one
        elif value_of_card(card_two) > value_of_card(card_one):
            return card_two

        # If cards are of the same value, put them into a tuple and return it
        elif value_of_card(card_two) == value_of_card(card_one):
            return tuple([card_one, card_two])
    else:
        print("Must have two valid entries for the cards. No value passed.")
        return None


# PREP
# Use value_of_card function to get values of both cards
# Calculate sum of both cards: 1- 10: A = 11; 11-20: A = 1;
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if value_of_card(card_one) and value_of_card(card_one):
        if 'A' in [card_one, card_two]:
            return 1
        elif 4 <= value_of_card(card_one) + value_of_card(card_two) <= 10:
            return 11
        elif value_of_card(card_one) + value_of_card(card_two) > 10:
            return 1
    else:
        print("Must have two valid entries for the cards. No value passed.")
        return None

# PREP
# Use value_of_card and add both cards based on their value
# Use conditional to check if sum is 21


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) and value_of_card(card_two):
        if ('A' in [card_one, card_two]) and any(card in [card_one, card_two] for card in ['10', 'J', 'Q', 'K']):
            return True
        else:
            return False
    else:
        print("Must have two valid entries for the cards. No value passed.")
        return None


# PREP
# Use higher_card function to see if a tuple is returned (this means both cards have the same value)
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    if type(higher_card(card_one, card_two)) == tuple:
        return True
    else:
        return False


# PREP
# Check if sum of cards is equal to 9-11; if so return True
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if value_of_card(card_one) and value_of_card(card_two):
        if value_of_card(card_one) + value_of_card(card_two) in range(9, 12):
            return True
        else:
            return False
