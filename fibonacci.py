
def fibonacci_generator():
    """A generator that yields numbers in the Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b 


# Example Usage
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))


"""
Output:
0
1
1
2
3
5
8
13
21
34
"""