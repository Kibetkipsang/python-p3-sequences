#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    elif length > 0:
        fib = []
        a, b = 0, 1
        while len(fib) < length:
            fib.append(a)
            a,b = b, a+b

    print(fib)  

print_fibonacci(10)     




