import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio import SeqIO


rec1, rec2 = [x for x in SeqIO.parse("rosalind_sample.txt", 'fasta')][:2]
transitions, transversions = 0, 0

dict = {
    frozenset(['A', 'G']): 'transition',
    frozenset(['C', 'T']): 'transition',
    frozenset(['A', 'C']): 'transversion',
    frozenset(['G', 'T']): 'transversion',
    frozenset(['A', 'T']): 'transversion',
    frozenset(['C', 'G']): 'transversion',
}

for s1, s2 in zip(str(rec1.seq), str(rec2.seq)):
    diff = dict.get(frozenset([s1, s2]))
    if diff:
        if diff == 'transition':
            transitions += 1
        elif diff == 'transversion':
            transversions += 1
print(transitions / transversions)

# Other rosalinder's solution
def tran(s, t):
    pairs = {'A':'G', 'G':'A', 'C':'T', 'T':'C'}
    transitions = [pairs[x] == y for x, y in zip(s, t) if x != y]
    print(1/(len(transitions)/sum(transitions)-1)) # equivalent to sum(transitions)/(len(transitions)-sum(transitions))

def tran(s, t):
    unchanged = sum(a == b for a, b in zip(s, t))
    transversion = sum((a in ('A', 'G')) != (b in ('A', 'G')) for a,b in zip(s,t))
    return (len(s)-transversion-unchanged) / transversion
