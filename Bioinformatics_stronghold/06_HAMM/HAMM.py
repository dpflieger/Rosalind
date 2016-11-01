def hamdist(str1, str2):
   """Count the # of differences between equal length strings str1 and str2"""
   diffs = 0
   for ch1, ch2 in zip(str1, str2):
       if ch1 != ch2:
           diffs += 1
   return diffs

seq = open('rosalind_hamm.txt').readlines()
seq1 = seq[0].strip()
seq2 = seq[1].strip()

print(hamdist(seq1, seq2))
