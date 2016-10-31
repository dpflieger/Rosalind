from Bio import SeqIO
from itertools import product, tee

records_a, records_b = tee(SeqIO.parse("rosalind_grph.txt", "fasta"))

with open("grph_output.txt", "w") as out:
    for record_a, record_b in product(records_a, records_b):
        if record_a.seq[-3:] == record_b.seq[:3]:
            print(record_a.id, record_b.id, file=out)
        if record_a.seq[3:] == record_b.seq[-3:]:
            print(record_a.id, record_b.id, file=out)
