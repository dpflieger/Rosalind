
a, b, c, d, e, f = open('rosalind_iev.txt').read().split()
nr_offspring = 2

def expected_offspring(a, b, c, d, e, f, nr_offspring):
    print(nr_offspring * (a + b + c + d*0.75 + e*0.5))

expected_offspring(int(a), int(b), int(c), int(d), int(e), int(f), nr_offspring)
