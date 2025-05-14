import csv

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return sequence

def read_blosum62(file_path):
    blosum62 = {}
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        amino_acids = next(reader)[1:]  # read the first row (amino acids)
        for i, row in enumerate(reader):
            for j, value in enumerate(row[1:]):  # skip the first column (amino acid)
                blosum62[(amino_acids[i], amino_acids[j])] = int(value)
    return blosum62

def global_alignment_score(seq1, seq2, blosum62):
    score = 0
    identical_count = 0
    for i in range(len(seq1)):
        score += blosum62[(seq1[i], seq2[i])]
        if seq1[i] == seq2[i]:
            identical_count += 1
    identity_percentage = (identical_count / len(seq1)) * 100
    return score, identity_percentage

if __name__ == "__main__":
    
    human_seq = read_fasta('F:\IBI(ZST)\IBI1_2024-25\Practical13\human_sod2.fasta')
    mouse_seq = read_fasta('F:\IBI(ZST)\IBI1_2024-25\Practical13\mouse_sod2.fasta')
    random_seq = read_fasta('F:\IBI(ZST)\IBI1_2024-25\Practical13\Random.FASTA')
    blosum62 = read_blosum62('F:\IBI(ZST)\IBI1_2024-25\Practical13\BLOSUM62_20x20.csv')  

    comparisons = [
        (human_seq, mouse_seq, "Human - Mouse"),
        (human_seq, random_seq, "Human - Random"),
        (mouse_seq, random_seq, "Mouse - Random")
    ]

    for seq1, seq2, comparison_name in comparisons:
        score, identity_percentage = global_alignment_score(seq1, seq2, blosum62)
        print(f"{comparison_name} Alignment:")
        print(f"Alignment Score: {score}")
        print(f"Percentage of Identical Amino Acids: {identity_percentage:.2f}%\n")