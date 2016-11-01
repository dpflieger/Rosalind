sequence = open('rosalind_dna.txt').read()
print(*(sequence.count(nucl) for nucl in 'ACGT'))
