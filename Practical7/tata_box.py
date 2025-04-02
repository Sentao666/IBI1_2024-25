import re

# Open the FASTA - formatted file containing the cDNA sequences of Saccharomyces cerevisiae.
# The 'with' statement ensures the file is automatically closed after operations.
with open(r"F:\IBI(ZST)\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r') as input_file:
    # A list to store processed gene information, elements are tuples of (gene name, gene sequence)
    processed_genes = []
    # Variable to record the name of the currently - processing gene
    current_gene_name = None
    # List to temporarily store fragments of the current gene sequence
    current_gene_sequence_fragments = []
    for line in input_file:
        # Remove leading and trailing whitespace from the line
        line = line.strip()
        # Check if it is the start line of a new gene sequence (starts with '>' in FASTA format)
        if re.search('>', line):
            # If a gene is currently being processed (i.e., current_gene_name is not None)
            if current_gene_name:
                # Add the name and complete sequence of the current gene to the processed_genes list
                processed_genes.append((current_gene_name[0], '\n'.join(current_gene_sequence_fragments)))
            # Extract the gene name from the line (assuming the gene name is after 'gene:')
            current_gene_name = re.findall(r'gene:(\S+)', line)
            # Clear the list of sequence fragments to prepare for storing the new gene's sequence
            current_gene_sequence_fragments = []
        else:
            # If it is not the start line of a new gene, it is a sequence fragment of the current gene, add it to the list
            current_gene_sequence_fragments.append(line)
    # After processing the file, check and add the last gene (if any)
    if current_gene_name:
        processed_genes.append((current_gene_name[0], '\n'.join(current_gene_sequence_fragments)))

# Open the target file for writing the filtered gene sequences.
# The 'with' statement ensures the file is automatically closed after operations.
with open(r'F:\IBI(ZST)\IBI1_2024-25\Practical7\tata_genes.fa', 'w') as output_file:
    # Iterate through the list of processed gene information
    for gene_name, gene_sequence in processed_genes:
        # Check if the gene sequence contains specific sequence patterns (TATATAT, TATATAA, TATAAAT, TATAAAA)
        if re.search(r'(TATATAT|TATATAA|TATAAAT|TATAAAA)', gene_sequence):
            # If a matching pattern is found, write the gene name and sequence to the target file
            output_file.write(f'> {gene_name}\n{gene_sequence}\n')