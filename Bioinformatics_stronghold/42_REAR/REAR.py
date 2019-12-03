from itertools import product

infile = "rosalind_sample.txt"

def reversesub(s, begin, end):
    return s[0:begin] + s[begin:end][::-1] + s[end:]

def get_all_reverse(s):
    ls = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            ls.append(reversesub(s, i, j))
    return ls 

def does_pass(seq1, seq2, i) :
    if sum(1 for idx, i in enumerate(seq1) if i == seq2[idx]) >= i:
        return True 
    return False 

def reversal_distance(seq1, seq2):
    if seq1 == seq2:
        return 0 
    elif seq1 == seq2[::-1]:
        return 1 
    else:
        ls = seq1
        i = 1
        while True :
            print(seq2)
            ls = {l for ll in ls for l in get_all_reverse(seq2) if does_pass(l, seq2, i)}
            print(ls)
            if any(l == seq2 for l in ls) :
                print("done")
                return i 
            i += 1
            if not ls :
                print("Stopped")
                exit()

with open(infile, "r") as f:
    data = [l.strip() for l in f.readlines()]
    lst = [(seq1.split(), seq2.split()) for seq1, seq2 in zip(data[0::3], data[1::3])]

    for seq1, seq2 in lst:
        print(seq1, seq2)
        print(reversal_distance(seq1, seq2))



    
