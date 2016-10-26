import itertools
from math import factorial
import sys


def partial_permutations(n, k):
	return int(factorial(n) / factorial(n-k) % 1000000)

if __name__ == '__main__':

    print(partial_permutations(100, 9))
