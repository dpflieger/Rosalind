from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

rna = Seq(open('rosalind_prot.txt').readline().strip())
prot = rna.translate(to_stop=True)
print(prot)
