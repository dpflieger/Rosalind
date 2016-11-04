from Bio import ExPASy
from Bio import SwissProt
import re

#proteins_ids = [protein_id.strip() for protein_id in open("rosalind_sample.txt").readlines()]
proteins_ids = [protein_id.strip() for protein_id in open("rosalind_mprt.txt").readlines()]
# N-glycosylation motif is written as N{P}[ST]{P}
motif = r"(?=(N[^P][ST][^P]))"

with open("rosalind_output.txt", "w") as out:
    for protein_id in proteins_ids:
        handle = ExPASy.get_sprot_raw(protein_id)
        record = SwissProt.read(handle)
        start_positions = [str(match.start() + 1) for match in re.finditer(motif, record.sequence)]
        if start_positions:
            print(protein_id, file=out)
            print(" ".join(start_positions), file=out)
