from bisect import bisect_left
import numpy as np

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -2) # don't walk off the end

infile = "rosalind_bins.txt"
#infile = "rosalind_sample.txt"
sorted_array = [*map(int, open(infile).readlines()[2].split())]
list_integers = [*map(int, open(infile).readlines()[3].split())]

with open("rosalind_output.txt", "w") as out:
    for i in list_integers:
        print(binary_search(sorted_array, i) + 1, end=" ", file = out)
