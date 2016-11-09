from Bio.Seq import Seq
from itertools import product
import re

#dna = Seq(open('rosalind_sample.txt').readline().strip())
dna = Seq(open('rosalind_orfr.txt').readline().strip())

with open("rosalind_orfr_result.txt", "w") as output:
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
    print(max(set(orfs), key=len), file=output)
