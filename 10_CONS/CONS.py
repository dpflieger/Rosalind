from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio.Seq import Seq
import numpy as np

#alignment = AlignIO.read("rosalind_sample.txt", "fasta")
alignment = AlignIO.read("rosalind_cons.txt", "fasta")

summary_align  = AlignInfo.SummaryInfo(alignment)

consensus = summary_align.dumb_consensus(threshold=0)
my_pssm = summary_align.pos_specific_score_matrix(consensus)

print(my_pssm)
