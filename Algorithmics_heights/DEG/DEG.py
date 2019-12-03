import networkx as nx
import matplotlib.pyplot as plt

#infile = "rosalind_sample.txt"
infile = "rosalind_deg.txt"


with open(infile, "r") as f:

    data = [l.strip() for l in f.readlines()]
    n_node, n_edge = map(int, data[0].split())

    print(n_node, n_edge)
    
    edges = [list(map(int, l.split())) for l in data[1::]]

    #print(edges)
    G = nx.Graph()
    G.add_edges_from(edges)

    #print(G)
    ## See the actual tree
    #nx.draw(G, with_labels = True)
    #plt.show()

    for node in range(1, n_node+1):
        #print(node, "-->", G.adj[node])
        print(G.degree[node], end = " ")
        
