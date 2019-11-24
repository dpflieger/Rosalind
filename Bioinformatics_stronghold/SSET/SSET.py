
#infile = "rosalind_sample.txt"
infile = "rosalind_sset.txt"

with open(infile, "r") as f:
    nset = int(f.readline().strip())
    nsubset = pow(2, nset, 1000000)
    print(nsubset)