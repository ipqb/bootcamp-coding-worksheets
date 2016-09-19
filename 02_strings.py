#!/bin/python

# Welcome to the string worksheet! Here we will be learning how to work with and manipulate strings

# The format of the fasta headers is:
# >Uniprot_id (uniprotAccesssion) protein name, specie, strain(if applicable) variant
fasta_header1 = ">E3EFL6_PAEPS (E3EFL6) Glutamine synthetase, Paenibacillus polymyxa, strain SC2 I10V"
fasta_header2 = ">GLNA_HUMAN (P15104) Glutamine synthetase, human S341C"
fasta_header3 = ">HEMH_HUMAN (P22830) Ferrochelatase, human WT"

fasta_list = []
fasta_list.append(fasta_header1)
fasta_list.append(fasta_header2)
fasta_list.append(fasta_header3)

def one_split():
	"""
	Splitting is a useful tool that allows us to split on any character
	(whitespace, newline, backslash, etc.) and returns the remaining parts as 
	a list. This is how it works:

	s.split(separator) 

	>>> myname = "Betty Ann White"
	>>> myname.split(" ")
	['Betty','Ann','White']

	Note: The separator gets removed from between the parts of the list.

	Write a function that splits a fasta header so you can return just the Uniprot accession.

	"""

	### Write your function here ###

def two_join():
	"""
	Join is the opposite of split. It returens a new string that is joined the 
	sequence of strings into one string

	separator.join(sequence)

	>>> "-".join(myname)
	'Betty-Ann-White'

	Write a function that joins a fasta header so that you can return just the Uniprot ID 
	followed by the variant with no white spaces (choose a character to join them!)
	
	"""

	### Write your function here ###

def three_slice():
	"""
	A string is made up of smaller components in the form of characters.
	Sometimes you need to use only a part of a string.
	Luckily, Python indexes the characters in strings (starting from 0, of course)!
	This allows us to take out larger pieces of a string than a single character-
	this is called slicing. Example:

	>>> myname[0:5]
	'Betty'

	The syntax for a slice is s[startIndex:pastIndex]
	Notice that the index after the colon is past the end of the slice.

	What does an index of [-1], or another negative number mean in a string?
	Guess, and then check yourself by looking it up. What would this return?

	>>> myname[-5:]
	???

	Then, write a function that slices a fasta header to return a list of the Uniprot
	Accession, a list of the species, and a list of the variants
	"""

	### Write your function here ###

def four_strip():
	"""
	Strip is another useful method that returns a string with whitespace removed. 

	s.strip()

	>>> myname.strip(" ")
	'BettyAnnWhite'

	Now, write a function that strips the parenthesis and the commas from the fasta headers
	"""

	### Write your function here ###

def other_methods():
	"""
	There are other useful string methods to play around with including:

	s.startswith('other'), s.endswith('other')
	s.replace('old','new')
	s.find('other')

	If you are unsure how to use these, look up some examples!

	Then try to apply them to the fasta header - 
	1. Return the beginning of every header
	2. Replace the protein name in the header with the gene name (you can just 
		make up a gene name - it doesn't need to be correct).
	3. Find every instance of the word "human" 
	"""

	### Write your function(s) here ###

for each in fasta_list:
	print one_split(each)
	print two_join(each)
	print three_slice(each)
	print four_strip(each)

