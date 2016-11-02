from Bio import ExPASy
from Bio import SwissProt

prot_id = str(open("rosalind_dbpr.txt").read().strip())

handle = ExPASy.get_sprot_raw(prot_id) #you can give a several ID divided by comma
record = SwissProt.read(handle) # SwissProt.parse for the several proteins

for f in record.cross_references:
    if 'P:' in f[2]:
         print(str(f[2]).strip('P:'))
