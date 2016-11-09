from Bio import SeqIO

quality_threshold = int(open("rosalind_bfil.txt").readlines()[0])

new_records = []

for record in SeqIO.parse("rosalind_bfil.txt", "fastq", alphabet=None):

    start, end = 0, len(record.seq)
    phred_scores = record.letter_annotations["phred_quality"]

    for quality in record.letter_annotations["phred_quality"]:
        if quality < quality_threshold and not start > end:
            start += 1
        else:
            break

    for quality in record.letter_annotations["phred_quality"][::-1]):
        if quality < quality_threshold and not start > end:
            end -= 1
        else:
            break

    record.letter_annotations = {}
    record.seq = record.seq[start:end]
    record.letter_annotations["phred_quality"] = phred_scores[start:end]
    new_records.append(record)

with open("rosalind_output.txt", "w") as out:
    SeqIO.write(new_records, out, "fastq")
