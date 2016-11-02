#sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
sequence = open('rosalind_ini.txt').read()
print(*(sequence.count(nucl) for nucl in 'ACGT'))
