from Bio import SeqIO
import numpy as np

# quality_threshold = int(open("rosalind_sample.txt").readlines()[0])
# print(len([record for record in SeqIO.parse("rosalind_sample.txt", "fastq") if np.mean(record.letter_annotations["phred_quality"]) < quality_threshold]))

quality_threshold = int(open("rosalind_phre.txt").readlines()[0])
print(len([record for record in SeqIO.parse("rosalind_phre.txt", "fastq") if np.mean(record.letter_annotations["phred_quality"]) < quality_threshold]))
