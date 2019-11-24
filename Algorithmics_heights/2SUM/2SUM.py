from operator import itemgetter
import numpy as np

#infile = "rosalind_sample.txt"
infile = "rosalind_2sum.txt"

nr_array, array_size = open(infile).readlines()[0].split()

with open(infile) as f:
    for line in f.readlines()[1:]:
        array = line.split()
        print(array[1831], array[2408])
        #print(array[77], array[144])
        #print("########")
        found = False
        results = []
        nmax = int(array_size)
        nparray = np.array(array).astype(np.int)
        for i, val in enumerate(array, start=1):
            npsubset = nparray + int(val)
            subset = npsubset.tolist()
            #print(subset)
            #z = next((i for i, x in enumerate(res.tolist()[0:nmax], start = 1) if x == 0), None)
            z = subset.index(0) + 1 if 0 in subset else False
            #print(z)
            if z and i < z:
                results.append((i, z))
                found = True        
        if found:
            a, b = sorted(results, key=itemgetter(1))[0]
            print(a, b)
        else:
            print(-1)       
                
            