from Bio import SeqIO
import sys

fasta_file = sys.argv[1]

with open("test.txt", mode='w', buffering=-1, encoding=None, errors=None, newline=None, closefd=True) as out:
    for record_a in SeqIO.parse(fasta_file, "fasta", alphabet=None):
        for record_b in SeqIO.parse(fasta_file, "fasta", alphabet=None):
            if record_a.seq == record_b.seq:
                pass
            if record_a.seq[-3:] == record_b.seq[:3]:
                print(record_a.id, record_b.id, sep=' ', end='\n', file=out, flush=False)
            if record_a.seq[3:] == record_b.seq[-3:]:
                print(record_a.id, record_b.id, sep=' ', end='\n', file=out, flush=False)
