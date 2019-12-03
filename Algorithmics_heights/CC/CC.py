import networkx as nx
import matplotlib.pyplot as plt

#infile = "rosalind_sample.txt"
infile = "rosalind_cc.txt"

with open(infile, "r") as f:

    lines = [line.strip() for line in f.readlines()]
    n_node, n_edge = map(int, lines[0].split())
    
    G = nx.parse_edgelist(lines[1:], nodetype = int, data=False, delimiter=" ")
    G.add_nodes_from(range(1, n_node+1))
    
    ## See the actual tree
    #nx.draw(G, with_labels = True)
    #plt.show()

    # Get connected components
    print(nx.connected_components(G))

    # Get length of the connected components
    print([len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)])

    # Get number of subgraphs 
    # return sum(1 for cc in connected_components(G))
    print(nx.number_connected_components(G))