import re

def find_first_cut_site(dna_sequence, enzyme_sequence):
    # check if sequences contain only A, C, G, T
    if not re.fullmatch(r'[ACGT]+', dna_sequence) or not re.fullmatch(r'[ACGT]+', enzyme_sequence):
        raise ValueError("Sequences must contain only 'A', 'C', 'G', and 'T'")
    match = re.search(enzyme_sequence, dna_sequence)
    if match:
        return match.start()
    else:
        return -1  

# example
dna = "ACGTAGCTAGCTAGGATCCGATCGGATCCGATC"
enzyme = "GATCC"
cut_site = find_first_cut_site(dna, enzyme)
print("First cut site found at position:", cut_site)