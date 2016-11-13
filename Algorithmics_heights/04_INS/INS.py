
#infile = "rosalind_sample.txt"
infile = "rosalind_ins.txt"

with open(infile) as f:
    array = f.readlines()[1].split()
    total_swap = 0
    for i in range(2, len(array) + 1):
        last_item = int(array[0:i][-1])
        total_swap += sum(int(elem) > last_item for elem in array[0:i])

    print(total_swap)
