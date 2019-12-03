import networkx as nx
import matplotlib.pyplot as plt

#infile = "rosalind_sample.txt"
infile = "rosalind_bf.txt"

with open(infile, "r") as f:

    lines = [line.strip() for line in f.readlines()]
    n_node, n_edge = map(int, lines[0].split())

    # Read as Directed Graph 
    G = nx.parse_edgelist(lines[1:], nodetype=int, data=(('weight',int),), delimiter=" ", create_using = nx.DiGraph)

    # # See the actual tree
    nx.draw(G, with_labels = True)
    plt.show()
  
    for i in range(1, n_node+1):
        try:
            print(nx.bellman_ford_path_length(G, 1, i), end = " ")
        except:
            print("x", end = " ")

