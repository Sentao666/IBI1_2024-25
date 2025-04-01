# Define the DNA sequence
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCTAA'
# Initialize the maximum intron length
max_length = 0
# Iterate through the sequence to find the start of an intron (GT)
for i in range(len(seq) - 1):
    if seq[i:i + 2] == 'GT':
        # Once GT is found, search for the end of the intron (AG)
        for j in range(i + 2, len(seq) - 1):
            if seq[j:j + 2] == 'AG':
                # Calculate the length of the current intron
                length = j - i + 2
                # Update the maximum length if the current length is greater
                if length > max_length:
                    max_length = length
# Print the maximum intron length
print(max_length)