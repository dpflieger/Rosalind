from Bio import SeqIO

quality_threshold, percent_of_base = open("rosalind_filt.txt").readlines()[0].split()
quality_threshold, percent_of_base = float(quality_threshold), float(percent_of_base)/100
print(len([record for record in SeqIO.parse("rosalind_filt.txt", "fastq") if sum(1 for base in record.letter_annotations["phred_quality"] if base >= quality_threshold)/len(record.seq) > percent_of_base]))
