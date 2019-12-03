import networkx as nx
import matplotlib.pyplot as plt

infile = "rosalind_sample.txt"
#infile = "rosalind_ddeg.txt"

with open(infile, "r") as f:

    lines = [line.strip() for line in f.readlines()]
    n_node, n_edge = map(int, lines[0].split())
    
    G = nx.parse_edgelist(lines[1:], nodetype = int, data=False, delimiter=" ")

    ## See the actual tree
    #nx.draw(G, with_labels = True)
    #plt.show()

    for node in range(1, n_node+1):
        try:
            neighbors_degree = G.degree(G.adj[node])
            print(sum(degree for _, degree in neighbors_degree), end = " ")
        except KeyError:
            print(0, end = " ")

