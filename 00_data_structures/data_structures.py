# Data Structures Activity
# Author: Seth Axen
# E-mail: seth.axen@gmail.com
# ========================
# Determining the best structure for a given type of data is a key first step
# in writing a given program.
# Python offers four key data structures: list, tuple, set, and dict. Several
# additional specialized structures come with Python and can be accessed by
# importing the 'collections' package. For numerical computing, additional
# data structures can be found in the NumPy, SciPy, and Pandas packages. In
# this assignment, you will practice choosing between the four default data
# structures.
#
# In this project, you will read in nucleotide FASTA sequences, determine
# which codons are present, translate to amino acids, count the frequencies
# of each amino acid in the sequence, and then print the amino acid FASTA
# sequence.

##
## Global variables
##

FILENAME = "seqs.fna"  # nucleotide FASTA file
# dict mapping nucleotide codons to amino acids.
CODON_TO_AA = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S',
               'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y',
               'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L',
               'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P',
               'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
               'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I',
               'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T',
               'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K',
               'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
               'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A',
               'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D',
               'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G',
               'GGG': 'G', 'TAA': '*', 'TAG': '*', 'TGA': '*'}
STOP_CODONS = set(['TAA', 'TAG', 'TGA'])  # set with stop codons


##
## Provided methods
## These are provided for convenience and as an example of file parsing
##

# Iterate through FASTA sequences in file. No need to understand how this
# works right now. In short, this method iterates through seqs in a file,
# yielding one-at-a-time, until all sequences are exhausted. This is more
# memory efficient than reading them all into memory at once!
# Usage:
#     for head, seq in fasta_seq_iter(seq_file):
#         do_something()
# Input: str
# Output: iterator of str, str
def fasta_seq_iter(filename):
    with open(filename, "rU") as f:
        head = None
        seq = ""
        for line in f:
            line = line.rstrip("\n")  # remove newline from end of line
            if line.startswith(">"):  # new sequence header
                if head is not None:  # if not first sequence in file...
                    yield head, seq  # yield the previous sequence
                head = line[1:].split(' ')[0]  # parse the header
                seq = ""  # reset sequence to empty
            else:
                seq += line  # append line to end of sequence
        yield head, seq  # yield last sequence in file


##
## Methods to fill out
## Fill in these methods to finish the code. ???s indicate data structures
## you will need to decide. You may want to write additional methods.
##

# Use the above method to iterate through sequences and store them.
# Input: str
# Output: ???
def seqs_from_file(filename):
    return []

# Split a sequence of nucleotides into codons.
# Input: ???
# Output: ???
def seq_to_codons(seq):
    return

# From sequence of possibly repeating codons, get sorted sequence of
# non-repeating amino acid-encoding codons present in input.
# Input: ???
def print_present_aa_codons(codons):
    return

# Translate sequence of codons to amino acids
# Input: ???
# Output: ???
def codons_to_aas(codons):
    return

# Count occurrence of amino acids and print in order of decreasing count
# Input: ???
def print_aa_counts(aas):
    print

# Get FASTA sequence as str
# Input: str, ???
# Output: ???
def get_aa_seq(head, aas):
    return


# Below will run when script is run with "python seq_data_struct.py"
if __name__ == "__main__":
    seqs = seqs_from_file(FILENAME)
    for head, seq in seqs:  # iterate through key, value pairs
        print(head + ":")
        codons = seq_to_codons(seq)
        print_present_aa_codons(codons)
        aas = codons_to_aas(codons)
        print("Amino acid frequencies:")
        print_aa_counts(aas)
        aa_seq = get_aa_seq(head, aas)
        print(str(aa_seq) + "\n")
