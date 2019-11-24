from Bio import Phylo
from io import StringIO

#infile = "rosalind_sample.txt"
infile = "rosalind_nwck.txt"

def add_default_branch_lengths(s, branch_length):
    insert = ':' + str(branch_length)
    s = s.replace(')', insert + ')')
    s = s.replace(',', insert + ',')
    s = s.replace(';', insert + ';')
    return s

with open(infile, "r") as f:

    data = [l.strip() for l in f.readlines()]
    trees = [(tree, node) for tree, node in zip(data[::3], data[1::3])]

    for tree, nodes in trees:
        ## Add default length to tree
        tree = add_default_branch_lengths(tree, 1)
        ## Read tree in newick format
        ntree = Phylo.read(StringIO(tree), "newick")

        ## nodes for distance
        node1, node2 = nodes.split()

        ## compute distance between nodes
        print(int(ntree.distance(node1, node2)), end=" ")

        ## See the actual tree
        # Phylo.draw(tree) # matplotlib
        # nx.draw(G)

