from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

dna_seq, protein_seq = map(Seq, open("rosalind_ptra.txt").read().splitlines())
nr_table = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 16, 21, 22, 23, 24, 25, 26]
[print(i) for i in nr_table if dna_seq.translate(table=i, stop_symbol='', to_stop=False) == protein_seq]
