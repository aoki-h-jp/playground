"""
Write a Python program to find the numbers of a given string and store them in a list,
display the numbers which are bigger than the length of the list in sorted form. Use lambda function to solve the problem.
Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
Numbers in sorted form:
20 23 56
"""
ORIG_STR = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"


if __name__ == '__main__':
    print(list(filter(lambda s: s.isdigit() and len(ORIG_STR.split(' ')) < int(s), ORIG_STR.split(' '))))
