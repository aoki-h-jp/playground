"""
48. Write a Python program to sort a given list of strings(numbers) numerically using lambda.
Original list:
['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
Sort the said list of strings(numbers) numerically:
['-500', '-12', '0', '4', '7', '12', '45', '100', '200']
"""
ORIG_LIST = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']


if __name__ == '__main__':
    print(sorted(ORIG_LIST, key=lambda n: int(n)))
