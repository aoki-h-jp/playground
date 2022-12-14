"""
10. Write a Python program to create Fibonacci series upto n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
from functools import reduce


if __name__ == '__main__':
    # PEP 8: E731 do not assign a lambda expression, use a def
    fib_series = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
    print(fib_series(2))
    print(fib_series(5))
    print(fib_series(6))
    print(fib_series(9))
