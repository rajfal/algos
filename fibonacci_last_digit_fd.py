# 
# Fast doubling Fibonacci algorithm (Python)
# 
# Copyright (c) 2015 Project Nayuki
# All rights reserved. Contact Nayuki for licensing.
# https://www.nayuki.io/page/fast-fibonacci-algorithms
# 
import sys

# (Public) Returns F(n).
def fibonacci(n):
    if n < 0:
        raise ValueError("Negative arguments not implemented")
    return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n, count=0):
    if n == 0:
        print(count)
        return (0, 1)
    else:
        a, b = _fib(n // 2, count=count+1)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)



# Recursive
def rec(a, b):
    if (b > a):
        return a
    else:
        return rec(a - 1, b+ 1)

# Iterative
def rec2(a, b):
    while b <= a:
        a = a - 1
        b = b + 1
    return a
    
print(rec2(30, 20))
