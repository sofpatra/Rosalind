# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 23:34:17 2025

@author: Sofiya
"""

def LongestCommonSubstring(k) -> str:
    #initialize longest common substring
    lcs = ''
    #sort the list of sequences by length
    k = sorted(k, key=len)
    #get the length of the first and shortest sequence
    shortest_seq = k[0]
    len1 = len(shortest_seq)
    #iterate over possible substring lengths
    for lens in range(1, len1+1):
        for j in range(len1 - lens +1):
            #generate substring
            string1=shortest_seq[j:j+lens]
            
            #check if substring is in all the other strings
            in_others = True
            for string in k[1:]:
                if string1 not in string:
                    in_others= False
                    break
            #if the string is in all the other strings and is longer than the 
            #current lcs update lcs to store the string 
            if in_others and len(string1) > len(lcs):
                lcs = string1
                break
    return lcs

sequences = []
with open("rosalind_lcsm.txt", "r") as file:
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


print(LongestCommonSubstring(sequences))
