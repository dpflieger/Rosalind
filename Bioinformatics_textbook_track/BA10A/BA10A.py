from collections import Counter
from itertools import product

#infile = "rosalind_sample.txt"
#infile = "rosalind_extra_dataset.txt"
infile = "rosalind_ba10a.txt"

observed_seq = open(infile).readlines()[0].strip()
states = open(infile).readlines()[2].split()
transitions = open(infile).readlines()[5].split()[1:] + open(infile).readlines()[6].split()[1:]

print(observed_seq) ; print(states) ; print(transitions)

# get transitions as dict
transition_dict = {"".join(trans): float(transitions[i]) for i, trans in enumerate(product("".join(states), repeat=2), 0)}
print(transition_dict)

# get the count of each transition
kmers_counter = Counter([observed_seq[i:i+2] for i in range(len(observed_seq)-1)])
print(kmers_counter)

prob = {key: transition_dict[key] ** kmers_counter[key] for key in transition_dict.keys()}

# initial probabilities are equal so --> 0.5
res = 0.5
for key, value in prob.items():
    res *= value

print(res)
