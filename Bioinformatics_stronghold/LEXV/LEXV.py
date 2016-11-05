from itertools import product

lines = open("rosalind_lexv.txt").readlines()
alphabet = lines[0].split()
n = int(lines[1])

mylist = []

# get all possible combination
for i in range(1, n+1):
    [mylist.append("".join(substring)) for substring in product(alphabet, repeat=i)]

# sort with new alphabet order
mylist_sorted = sorted(mylist, key=lambda order: [alphabet.index(c) for c in order])

with open("rosalind_output.txt", "w") as out:
    [print(value, file = out) for value in mylist_sorted]
