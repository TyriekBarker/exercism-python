from enum import Enum


def convert(number):
    # Add empty string to hold final value of the sound
    raindrop = ""
    # Represent different sounds as enumerated values
    RaindropSound = Enum("RaindropSound", ["Pling", "Plang", "Plong"])
    # For each divisor, test if the number passed into the function has it as a factor;
    # if so, add the the corresponding enumerated value to the final string
    if not number % 3:
        raindrop += RaindropSound(1).name
    if not number % 5:
        raindrop += RaindropSound(2).name
    if not number % 7:
        raindrop += RaindropSound(3).name
    # Return the number passed into the function if no divisor is a factor;
    # otherwise return the final string
    if not raindrop:
        return str(number)
    return raindrop
