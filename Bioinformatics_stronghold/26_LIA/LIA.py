from math import factorial

def binomial(n,k):
    return(factorial(n) / (factorial(k) * factorial(n-k)))

def comb(n, k):
    'Equivalent to factorial(n) // (factorial(k) * factorial(n-k))'
    c = 1
    k = min(k, n-k)
    for i in range(1, k+1):
        c = c * (n - k + i) // i
    return c

def P(n, k):
    return(comb(2**k, n) * 0.25**n * 0.75**(2**k - n))

#infile = 'rosalind_sample.txt'
infile = 'rosalind_lia.txt'

with open(infile, 'r') as f:
    k, N = map(int, f.readline().split())
    res = 1 - sum([P(n, k) for n in range(N)])
    print(round(res, 3))
