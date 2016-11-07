from Bio import SeqIO
import numpy as np

quality_threshold = int(open("rosalind_bphr.txt").readlines()[0])
mylist = [record.letter_annotations["phred_quality"] for record in SeqIO.parse("rosalind_bphr.txt", "fastq")]
mat = np.array(mylist)
mean_position_qualities = mat.mean(axis=0)
print(sum(1 for mean_position_quality in list(mean_position_qualities) if mean_position_quality < quality_threshold))
