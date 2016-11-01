from itertools import permutations

n = 3

# easy with itertools permutation
permut = list(permutations(range(1, n+1)))
# write to file for large n
with open("rosalind_perm_results.txt", "w") as outfile:
    print(len(permut), file = outfile)
    [print(" ".join(list(map(str, i))), file = outfile) for i in permut]
