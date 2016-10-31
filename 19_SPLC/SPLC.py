from Bio import SeqIO
from Bio.Seq import Seq

#records = SeqIO.parse("rosalind_sample.txt", "fasta")

records = SeqIO.parse("rosalind_splc.txt", "fasta")
dna_sequence = str(next(records).seq)

for record in records:
    intron = str(record.seq)
    dna_sequence = dna_sequence.replace(intron, "")

print(Seq(dna_sequence).translate(to_stop = True))
