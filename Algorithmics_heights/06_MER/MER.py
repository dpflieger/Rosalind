from itertools import product

#infile = "rosalind_sample.txt"
infile = "rosalind_mer.txt"

first_array =  list(map(int, open(infile).readlines()[1].split()))
second_array = list(map(int, open(infile).readlines()[3].split()))

with open("rosalind_output.txt", "w") as out:
    print(" ".join(list(map(str, sorted(first_array + second_array)))), file=out)


def merge_sort(a, b):
    """
    A nice merge sort popping out items from both lists and running until both
    are empty
    """
    l = []
    while a and b:
        if a[0] < b[0]:
            l.append(a.pop(0))
        else:
            l.append(b.pop(0))
    return l + a + b

print(merge_sort(first_array, second_array))
