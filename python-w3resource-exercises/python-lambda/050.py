"""
50. Write a Python program to remove specific words from a given list using lambda.
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']
Remove words:
['orange', 'black']
After removing the specified words from the said list:
['red', 'green', 'blue', 'white']
"""
ORIG_LIST = ['orange', 'red', 'green', 'blue', 'white', 'black']
REMOVE_WORDS = ['orange', 'black']


if __name__ == '__main__':
    print(list(filter(lambda s: s not in REMOVE_WORDS, ORIG_LIST)))
