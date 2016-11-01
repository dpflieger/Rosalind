from math import factorial
from Bio import SeqIO
import sys

def perfect_matching(seq):

    print(factorial(seq.count('A')) * factorial(seq.count('C')))

if __name__ == '__main__':

    sequence = SeqIO.read(sys.argv[1], "fasta").seq

    perfect_matching(sequence)
