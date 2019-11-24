#lines = open('rosalind_sample.txt').readlines()

lines = open('rosalind_seto.txt').readlines()

n, A, B = int(lines[0]), eval(lines[1]), eval(lines[2])
cset = set(range(1, n+1))

with open("results.txt", "w") as out:
    # A ∪ B
    print(A | B, file = out) 
    # A ∩ B
    print(A & B, file = out)
    # A−B
    print(A - B, file = out)
    # B−A
    print(B - A, file = out)
    # Ac
    print(cset - A, file = out)
    # Bc
    print(cset - B, file = out)