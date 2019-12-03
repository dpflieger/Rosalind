import networkx as nx
import matplotlib.pyplot as plt
import itertools

#infile = "rosalind_sample.txt"
infile = "rosalind_sq.txt"

with open(infile, "r") as f:

    lines = [line for line in f.read().split("\n\n")]
    #print(lines)

    n = int(lines[0].strip())
    #print("Number of graph:", n)

    edges_list = [edge.split("\n") for edge in lines[1:]]
    #print(graph_list)

    def lmap(func, x):
        return(list(map(func, x)))

    for edgelist in edges_list:
        
        G = nx.parse_edgelist(edgelist, nodetype=int, data=False, delimiter=" ")

        G.add_nodes_from(range(1, n+1))

        #H = nx.DiGraph(G)

        #print(nx.cycle_basis(G))
    
        

        ## See the actual tree
        #nx.draw(G, with_labels = True, edgecolors="green")
        #plt.show()

        #print(nx.cycle_basis(G))
        #print(list(nx.simple_cycles(H)))
        a = -1

        for cycle in nx.cycle_basis(G):
            if len(cycle) == 4:
                a = 1
                break
        print(a, end = " ")


""" Best implementation !!!
from itertools import combinations

def graph_has_square_cycle(G):
    for v, neighbors in G.items():
        for u, w in combinations(neighbors, 2):
            if G[u] & G[w] - {v}:  # check if sets intersection (minus the common vertex v) length > 0
                return 1
    return -1
"""

"""
import numpy as np

def has_square(adj_matrix):

    len_of_walk = 2
    A_squared_diag_zero = np.linalg.matrix_power(adj_matrix, len_of_walk)
    np.fill_diagonal(A_squared_diag_zero, 0)

    if np.any(A_squared_diag_zero > 1):
        return 1
    return -1
"""