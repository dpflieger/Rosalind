from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    return (pos if pos != hi and a[pos] == x else -2)

infile = "rosalind_bins.txt"
sorted_array = [*map(int, open(infile).readlines()[2].split())]
list_integers = [*map(int, open(infile).readlines()[3].split())]

with open("rosalind_output.txt", "w") as out:
    for i in list_integers:
        print(binary_search(sorted_array, i) + 1, end=" ", file = out)
