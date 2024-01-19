# Read the full-length protein sequence from the file
with open('full_length.dat', 'r') as file:
    full_protein_sequence = file.read()

# Define the length of each sequence
sequence_length = 25             #replace this number with appropriate peptide length

# Initialize an empty list to store the sequences
sequences = []

# Extract sequences of the specified length
for i in range(len(full_protein_sequence) - sequence_length + 1):
    sequence = full_protein_sequence[i:i + sequence_length]
    sequences.append(sequence)

# Print the list of sequences
for i, sequence in enumerate(sequences):
    print(f"Seq {i + 1}: {sequence}")

# If you want to save the sequences to a file:
with open('output_sequences.txt', 'w') as output_file:
     for i, sequence in enumerate(sequences):
         output_file.write(f"Seq{i + 1} {sequence}\n")

