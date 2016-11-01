from Bio import SeqIO
from itertools import product

for record in SeqIO.parse("rosalind_revp.txt", "fasta"):
    for i in range(len(record.seq)):
        for j in range(4, min(13, len(record.seq) - i + 1)):
            ss = record.seq[i:i+j]
            if str(ss) == str(ss.reverse_complement()):
                print(i+1, j)
