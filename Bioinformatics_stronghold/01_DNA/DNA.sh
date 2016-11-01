awk '{a=gsub("A","");c=gsub("C","");g=gsub("G","");t=gsub("T","")} END {print a,c,g,t}' rosalind_dna.txt
