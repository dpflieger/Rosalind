from Bio import SeqIO
print((sum(1 for record in SeqIO.parse("rosalind_rvco.txt", "fasta") if record.seq == record.seq.reverse_complement())))
