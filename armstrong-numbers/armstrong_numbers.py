# PREP
# Test if the sum of x**NUMBER_OF_DIGITS for each digit in a number is equal to that number
def is_armstrong_number(number):
    # Conversion into string and then list
    formatted_number = str(number)
    number_list = list(formatted_number)
    NUMBER_OF_DIGITS = len(number_list)
    # Value to compare number to
    total = 0

    # Get Armstrong value
    for num in number_list:
        total += int(num)**NUMBER_OF_DIGITS

    # Check if original value is an Armstrong number If it is return true...
    if total == number:
        return True

    # ...if it is not, return false
    return False
