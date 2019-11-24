import sys
import operator
import networkx as nx
import matplotlib.pyplot as plt
from functools import reduce

with open(sys.argv[1], "r") as infile:
    # Total nodes
    n = infile.readline().strip()

    # Actual nodes in the list 
    nodes = [tuple(line.strip().split()) for line in infile.readlines()]
    #print(nodes)

    # Flatten list
    #unique_nodes = reduce(operator.concat, nodes)
    
    G = nx.Graph()
    G.add_edges_from(nodes)

    components = nx.connected_components(G) 
    nr_components = sum(1 for _ in components)
    #print(nr_components)
    print(nx.number_connected_components(G))


    def min_edges_for_tree(n, G):

        missing_nodes = int(n) - G.number_of_nodes()
        # 1 missing node with 3 group = 3 edges to make a tree
        # 2 missing node with 3 group = 4 edges to make a tree
        components = nx.connected_components(G) 
        nr_components = sum(1 for _ in components)
        return(nr_components + missing_nodes - 1)

    print(min_edges_for_tree(n, G))


    # print(G.nodes())
    # print(G.edges())
    # print(G.number_of_nodes())
    # print(G.number_of_edges())
    # print(list(nx.non_edges(G)))
    # print(G.degree())
    # print(nx.info(G))
    
    # Draw/show the graphs 
    #nx.draw(G)
    #plt.show()

    #print(list(G))

    #actual_nodes = list(dict.fromkeys(unique_nodes))


    # Get number of graph


    # Number of edge required to get a tree from the graphs
    # n_edges = 


    #print(len(nodes))
    #print(nodes)
