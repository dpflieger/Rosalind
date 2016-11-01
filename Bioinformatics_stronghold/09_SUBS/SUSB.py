from Bio import motifs
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

sequence, motif = open('rosalind_subs.txt').read().splitlines()
#sequence, motif = open('rosalind_sample.txt').read().splitlines()

instances = [Seq(motif)]
m = motifs.create(instances)

for pos, seq in m.instances.search(sequence):
    print(pos+1, end=' ')
