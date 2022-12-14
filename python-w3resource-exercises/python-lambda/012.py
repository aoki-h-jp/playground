"""
12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]
"""
ORIG_LIST = [-1, 2, -3, 5, 7, 8, 9, -10]


if __name__ == '__main__':
    print(sorted(ORIG_LIST, key=lambda i: 0 if i == 0 else -1 / i))
