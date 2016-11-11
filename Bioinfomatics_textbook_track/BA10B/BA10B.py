from collections import Counter
from itertools import product

#infile = "rosalind_sample.txt"
#infile = "rosalind_extra_dataset.txt"
infile = "rosalind_ba10b.txt"

observed_seq = open(infile).readlines()[0].strip()
alphabets = open(infile).readlines()[2].split()
pi = open(infile).readlines()[4].strip()
states = open(infile).readlines()[6].split()
transitions = open(infile).readlines()[9].split()[1:] + open(infile).readlines()[10].split()[1:]

print(observed_seq, alphabets, pi, states, transitions, sep = "\n")

# get transitions as dict
transition_dict = {"".join(x): float(transitions[i]) for i, x in enumerate(product(states, alphabets), 0)}
print(transition_dict)

# get the count of each transition
kmers_counter = Counter([b+a for a,b in zip(observed_seq, pi)])
print(kmers_counter)

prob = {key: transition_dict[key] ** kmers_counter[key] for key in transition_dict.keys()}

res = 1
for key, value in prob.items():
    res *= value

print(res)
