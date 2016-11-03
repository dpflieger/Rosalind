from itertools import product

#input1, input2 = open("rosalind_sample.txt", "r").readlines()
input1, input2 = open("rosalind_lexf.txt", "r").readlines()

print(input1, input2)

sequence = "".join([x.strip() for x in input1])
n = int(input2)

with open("rosalind_output.txt", "w") as out:
    for i in list(product(sorted(sequence), repeat=n)):
        print("".join(i), file = out)
