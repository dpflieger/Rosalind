from Bio import SeqIO

fasta_file = "rosalind_grph.txt"

with open("solution.txt", "w") as out:
    for record_a in SeqIO.parse(fasta_file, "fasta"):
        for record_b in SeqIO.parse(fasta_file, "fasta"):
            if record_a.seq == record_b.seq:
                pass
            if record_a.seq[-3:] == record_b.seq[:3]:
                print(record_a.id, record_b.id, file=out)
            if record_a.seq[3:] == record_b.seq[-3:]:
                print(record_a.id, record_b.id, file=out)
