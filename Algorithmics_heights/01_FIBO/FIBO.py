def fib(n):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

print(fib(24))
