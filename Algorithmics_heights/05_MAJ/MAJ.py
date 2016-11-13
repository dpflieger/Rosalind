from collections import Counter

#infile = "rosalind_sample.txt"
infile = "rosalind_maj.txt"

nr_array, array_size = open(infile).readlines()[0].split()
print(nr_array, array_size)

with open(infile) as f:
    for line in f.readlines()[1:]:
        array = Counter(line.split())
        for i in array.most_common(1):
            if i[1] <= int(array_size)/2:
                print("-1", end=" ")
            else:
                print(i[0], end=" ")

# and with a oneliner
def maj_elem(a):
    return Counter(a).most_common(1)[0] if Counter(a).most_common(1)[1] > len(a)/2 else -1
