"""
2. Write a Python program to iterate over an enum class and display individual member and their value.
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
"""
from enum import Enum


class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672


if __name__ == '__main__':
    for c in Country:
        print(f'{c.name} = {c.value}')
