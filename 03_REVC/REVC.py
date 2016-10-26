from Bio.Seq import Seq

print(Seq(open("rosalind_revc.txt").read()).reverse_complement())
