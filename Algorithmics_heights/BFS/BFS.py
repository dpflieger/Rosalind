import networkx as nx
import matplotlib.pyplot as plt

#infile = "rosalind_sample.txt"
infile = "rosalind_bfs.txt"

"""
An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to −1.
"""

with open(infile, "r") as f:

    lines = [line.strip() for line in f.readlines()]
    n_node, n_edge = map(int, lines[0].split())
    
    #print(lines[1::])

    # Convert to a Directed Graph 
    G = nx.parse_edgelist(lines[1:], nodetype=int, data=False, delimiter=" ", create_using = nx.DiGraph)
    #assert nx.is_directed_acyclic_graph(G)

    # Convert to a DAG (Directed Acyclic Graph)
    #T = nx.DiGraph([(u,v) for (u,v) in G.edges() if u<v])
    
    # # See the actual tree
    #nx.draw(G, with_labels = True)
    #plt.show()
  
    ## Remove selfloop 
    #H.remove_edges_from(nx.selfloop_edges(G))

    for i in range(1, n_node+1):
        try:
            print(nx.shortest_path_length(G, 1, i), end = " ")
        except:
            print("-1", end = " ")

