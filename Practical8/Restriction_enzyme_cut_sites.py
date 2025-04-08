def find_restriction_sites(dna_sequence, enzyme_sequence):
    valid_nucleotides = set('ACGT')
    # Check whether the DNA sequence contains only standard nucleotides
    if not all(nucleotide in valid_nucleotides for nucleotide in dna_sequence):
        raise ValueError("DNA sequence contains non - canonical nucleotides")
    # Check if the enzyme recognition sequence contains only standard nucleotides
    if not all(nucleotide in valid_nucleotides for nucleotide in enzyme_sequence):
        raise ValueError("Enzyme recognition sequence contains non - canonical nucleotides")

    cut_sites = []
    len_enzyme = len(enzyme_sequence)
    for i in range(len(dna_sequence) - len_enzyme + 1):
        if dna_sequence[i:i + len_enzyme] == enzyme_sequence:
            cut_sites.append(i)
    return cut_sites

# Sample call
if __name__ == "__main__":
    try:
        dna = "ACGTACGTACGT"
        enzyme = "CGTA"
        result = find_restriction_sites(dna, enzyme)
        print(f"The restriction enzyme cut sites are: {result}")
    except ValueError as e:
        print(f"Error: {e}")