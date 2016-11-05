from Bio import SeqIO
from itertools import product
from collections import Counter

# get first sequence
#sequence = str(next(SeqIO.parse(open("rosalind_sample.txt"), "fasta")).seq)
sequence = str(next(SeqIO.parse(open("rosalind_kmer.txt"), "fasta")).seq)

# get all possible 4-mers
n = 4
kmers_dict = {"".join(kmer): 0 for kmer in product("ATGC", repeat=n)}

# count 4-mers in sequence
kmers_counter = Counter([sequence[i:i+n] for i in range(len(sequence)-(n-1))])

# merge the dicts
z = {**kmers_dict, **kmers_counter}

# save kmers count
with open("rosalind_output.txt", "w") as out:
    [print(count, end=' ', file=out) for kmer, count in sorted(z.items())]
