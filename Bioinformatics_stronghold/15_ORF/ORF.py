from Bio import SeqIO
from itertools import product
import re

#dna = SeqIO.read("rosalind_sample.txt", "fasta").seq
dna = SeqIO.read("rosalind_orf.txt", "fasta").seq

with open("rosalind_orf_result.txt", "w") as output:
    orfs = []
    # check both strands and their frames
    for strand, frame in product([dna, dna.reverse_complement()], range(3)):
        # get full translation
        proteic_seq = str(strand[frame:].translate())
        # get ORFs, all regions starting with "M" and ending with "*"
        matches = re.findall('(?=(M.*?)\*)', proteic_seq)
        #if matches:
        for match in matches:
            orfs.append(match)

    # use set to get distinct sequence as specified
    print("\n".join(set(orfs)), file=output)
