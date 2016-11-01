def fib(n, k):
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, k*a + b
    return b

n, k = open("rosalind_fib.txt").read().split()

print(fib(int(n), int(k)))
