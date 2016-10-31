from Bio.SeqUtils import CodonUsage, seq1

aa_seq = open('rosalind_mrna.txt').read().strip()

# Conversion of Biopython's CodonTable to a frequence table, codon stop = "X" here
codons_freq = {seq1(aa): len(codons) for aa, codons in CodonUsage.SynonymousCodons.items()}
count = 1
for aa in aa_seq:
    count *= codons_freq[aa]

# Print count with codon stop possibility at the end of a sequence
print(count * codons_freq["X"] % 1000000)
