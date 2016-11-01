from Bio import SeqIO
from Bio.SeqUtils import GC

record_id, highest_gc = None, 0

for record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    gc = round(GC(record.seq), 6)
    if gc > highest_gc : highest_gc, record_id = gc, record.id

print(record_id, highest_gc, sep='\n')
