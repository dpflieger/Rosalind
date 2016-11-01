from Bio import SeqIO
import sys
from itertools import cycle

def subsequence(seq1, seq2):
    #print(seq1)
    #print(seq2)

    index = 1
    sequence = []
    for base2 in seq2:
        for base1 in seq1[index-1:]:
            if base2 == base1:
                sequence.append(index)
                index += 1
                break
            else:
                index += 1

    print(" ".join(map(str, sequence)))


if __name__ == '__main__':

    record1, record2 = SeqIO.parse(sys.argv[1], "fasta")
    subsequence(str(record1.seq), str(record2.seq))
