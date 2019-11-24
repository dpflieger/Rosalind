from Bio import Phylo
from io import StringIO

c = open('rosalind_nwck.txt').read().rstrip().split('\n\n')

for i in c:
    t, x, y = i.split()
    tree = Phylo.read(StringIO(t), 'newick')
    ancestor = tree.common_ancestor(x, y)
    print(len(ancestor.get_path(x)) + len(ancestor.get_path(y)), end = " ")

#open('rosalind_nwck_sub.txt', 'wt').write(' '.join([str(i) for i in out]))