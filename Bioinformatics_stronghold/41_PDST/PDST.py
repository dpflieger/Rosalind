import sys
import numpy as np
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator

aln = AlignIO.read(sys.argv[1], "fasta")
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(aln)
res = np.array(dm)

np.savetxt("results.txt", res, fmt='%.4f') 