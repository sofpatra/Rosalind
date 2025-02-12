# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:34:31 2025
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s
 (of length at most 1 kbp) and a collection of substrings of s
 acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s
. (Note: Only one solution will exist for the dataset provided.)

@author: Sofiya
"""

codon_dict = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F','CUC': 'L', 'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V','UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 'ACU': 'T','GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S', 'CCA': 'P','ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU': 'Y','CAU': 'H', 'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D','UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K','GAG': 'E', 'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R','AGC': 'S', 'GGC': 'G', 'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W','CGG': 'R', 'AGG': 'R', 'GGG': 'G'}


def Translation(s: str) -> str:
    #initialize protein string
    protein = ""
    #ensure string is all uppercase 
    s = s.upper()
    #find 'AUG' to begin translation
    s = s[s.find("AUG"):]
    #iterate through the length of the new sequence starting with AUG in steps of 3 
    for i in range(0, len(s)-2, 3):
        # Extract codon (3 nucleotides)
        codon = s[i:i+3] 
        #check if codon is in the codon table
        if codon in codon_dict:
            # Translate codon to amino acid
            if codon_dict[codon] != 'Stop': 
                protein += codon_dict[codon]
                
        #Raise Key Error in case of non nucleotide string. 
        else:
            raise KeyError("Encountered a codon not part of the codon dictionary.") 
    return protein

#Read FASTA file 
sequences = []
with open("rosalind_splc.txt", "r") as file:
    seq = ""
    for line in file:
        line = line.strip()
        if line.startswith(">"):  # Header line
            if seq:  
                sequences.append(seq)
                seq = ""
        else:
            seq += line

    if seq:  # Append the last sequence in the file
        sequences.append(seq)

#print(sequences)
#subset FASTA
unspliced = sequences[0]
introns = sequences[1:]

def RNASplicing(unspliced: str, introns: list[str]) -> str:
    #iterate through the introns in the intron list 
    for intron in introns:
        #remove the intron from the string 
        unspliced = unspliced.replace(intron, '')
    #convert the string to mRNA by replacing T with U 
    unspliced = unspliced.replace('T', 'U')
    #translate the string into protein using previously defined function 
    protein = Translation(unspliced) 
    return protein

print(RNASplicing(unspliced, introns))
