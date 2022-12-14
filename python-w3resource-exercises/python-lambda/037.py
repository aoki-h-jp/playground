"""
37. Write a Python program to sort a list of lists by a given index of the inner list using lambda.
Original list:
[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
Sort the said list of lists by a given index ( Index = 0 ) of the inner list
[('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
Sort the said list of lists by a given index ( Index = 2 ) of the inner list
[('Wyatt Knott', 91, 94), ('Brady Kent', 97, 96), ('Beau Turnbull', 94, 98), ('Greyson Fulton', 98, 99)]
"""
ORIG_LIST = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]


if __name__ == '__main__':
    # PEP 8: E731 do not assign a lambda expression, use a def
    index_sort = lambda l, n: sorted(l, key=lambda x: x[n])
    print(index_sort(ORIG_LIST, 0))
    print(index_sort(ORIG_LIST, 2))
