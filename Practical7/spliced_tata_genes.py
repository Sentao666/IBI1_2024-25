import re

# Define the list of valid splice donor/acceptor combinations
valid_combinations = ['GTAG', 'GCAG', 'ATAC']
# Continuously ask for user input until a valid combination is provided
while True:
    user_input = input(f"Please enter one of the splice donor/acceptor combinations {valid_combinations}: ")
    if user_input in valid_combinations:
        break
    print("Invalid input. Please try again.")

# Path to the original FASTA file
input_file_path = r"F:\IBI(ZST)\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
# List to store processed gene information, elements are tuples of (gene name, gene sequence)
processed_genes = []
# Regular expression pattern for TATA boxes
tata_pattern = r'(TATATAT|TATATAA|TATAAAT|TATAAAA)'

# Open the original FASTA file for reading
with open(input_file_path, 'r') as input_file:
    current_gene_name = ""
    current_gene_sequence_fragments = []
    for line in input_file:
        line = line.strip()
        if line.startswith('>'):
            if current_gene_name:
                # Concatenate gene sequence fragments and remove line breaks
                full_sequence = "".join(current_gene_sequence_fragments)
                # Count the number of occurrences of TATA boxes
                tata_count = len(re.findall(tata_pattern, full_sequence))
                if tata_count > 0:
                    new_gene_name = f"{current_gene_name}_{tata_count}"
                    processed_genes.append((new_gene_name, full_sequence))
            # Extract the gene name (remove other information)
            match = re.search(r'gene:(\S+)', line)
            if match:
                current_gene_name = match.group(1)
            else:
                current_gene_name = ""
            current_gene_sequence_fragments = []
        else:
            current_gene_sequence_fragments.append(line)
    # Process the last gene
    if current_gene_name:
        full_sequence = "".join(current_gene_sequence_fragments)
        tata_count = len(re.findall(tata_pattern, full_sequence))
        if tata_count > 0:
            new_gene_name = f"{current_gene_name}_{tata_count}"
            processed_genes.append((new_gene_name, full_sequence))

# Generate the output file name
output_filename = f"{user_input}_spliced_genes.fa"
# Open the output file for writing
with open(output_filename, 'w') as output_file:
    for gene_name, gene_sequence in processed_genes:
        output_file.write(f'>{gene_name}\n{gene_sequence}\n')
    