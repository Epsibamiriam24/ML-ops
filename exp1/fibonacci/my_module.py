def fibonacci_upto(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    fib_seq = []
    a, b = 0, 1
    while a <= n:
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq
