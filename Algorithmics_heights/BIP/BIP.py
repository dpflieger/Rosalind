import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt

#infile = "rosalind_sample.txt"
infile = "rosalind_bip.txt"

with open(infile, "r") as f:

    lines = [line for line in f.read().split("\n\n")]
    n = int(lines[0].strip())
    #print("Number of graph:", n)

    edges_list = [edge.split("\n") for edge in lines[1:]]
    #print(graph_list)

    for edgelist in edges_list:
        
        G = nx.parse_edgelist(edgelist, nodetype=int, data=False, delimiter=" ")

        G.add_nodes_from(range(1, n+1))

        #H = nx.DiGraph(G)

        #print(nx.cycle_basis(G))
    
        if bipartite.is_bipartite(G):
            print(1, end = " ") 
        else:
            print(-1, end = " ")

        ## See the actual tree
        #nx.draw(G, with_labels = True, edgecolors="green")
        #plt.show()
