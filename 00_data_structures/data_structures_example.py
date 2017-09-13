# Data Structures Activity - Example Solution
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

# Iterate through FASTA sequences in file.
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
## Fill in these methods to finish the code
##

# Use the above method to iterate through sequences and store them.
# Input: str
# Output: dict
def seqs_from_file(filename):
    seq_dict = {}  # empty dict
    for head, seq in fasta_seq_iter(filename):
        seq_dict[head] = seq
    return seq_dict


# Split a sequence of nucleotides into codons.
# Input: str
# Output: list of str
def seq_to_codons(seq):
    seq_len = len(seq)
    assert(seq_len % 3 == 0)  # sequence length must be multiple of 3
    # use list comprehension to get length 3 string slices starting every 3
    # characters
    return [seq[i:i + 3] for i in range(0, seq_len, 3)]


# From sequence of possibly repeating codons, get sorted sequence of
# non-repeating amino acid-encoding codons present in input.
# Input: list of str
# Output: list of str
def get_present_aa_codons(codons):
    codon_set = set(codons)  # Convert to set. Removes duplicates and ordering
    return sorted(codon_set.difference(STOP_CODONS))  # sort non-stop codons.


# Translate codon to amino acid
# Input: str
# Output: str
def codon_to_aa(codon):
    return CODON_TO_AA.get(codon, "X")  # default to "X" if codon does not exist.


# Count occurrence of amino acids
# Input: list of str
# Output: dict (str => int)
def print_aa_counts(aas):
    aa_counts = {x: 0 for x in CODON_TO_AA.values()}  # initialize values
    for aa in aas:
        aa_counts[aa] += 1
    # sort by decreasing count
    for aa, count in sorted(aa_counts.items(), key=lambda x: (x[1], x[0]), reverse=True):
        print(aa + ": " + str(count))


# Get FASTA sequence as str
# Input: list of str
# Output: str
def get_aa_seq(head, aas):
    return ">" + head + "\n" + "".join(aas).rstrip("*")


# Below will run when script is run with "python seq_data_struct.py"
if __name__ == "__main__":
    seqs = seqs_from_file(FILENAME)
    for head, seq in seqs.items():  # iterate through key, value pairs
        print(head + ":")
        codons = seq_to_codons(seq)
        present_codons = get_present_aa_codons(codons)
        print("Codons in sequence: " + ", ".join(present_codons))
        # list comprehension: a fast way to create lists "on-the-fly"
        aas = [codon_to_aa(codon) for codon in codons]
        print("Amino acid frequencies:")
        print_aa_counts(aas)
        aa_seq = get_aa_seq(head, aas)
        print(aa_seq + "\n")
