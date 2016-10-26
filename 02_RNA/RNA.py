from Bio.Seq import Seq

print(Seq(open("rosalind_rna.txt").read()).transcribe())
