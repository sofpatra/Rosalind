# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:30:45 2025
Problem
Given two strings s and t, t is a substring of s if t is contained as a 
contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to 
its left, including itself (e.g., the positions of all occurrences of 'U' in 
"AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the 
starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", 
then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will 
have multiple locations in s if it occurs more than once as a substring of s
(see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
@author: Sofiya
"""



def FindingMotif(s: str, t: str):
    #check if length of motif is shorter than string 
    if len(s) < len(t): 
        raise ValueError("String 1 must be longer than string string 2.")
    
    #ensure strings are all uppercase 
    s = s.upper()
    t= t.upper()
    
    #initialize index list 
    loc = []
    
    #iterate through the length of the string minus the length of the substring 
    for i in range(0, len(s)- len(t) +1):
    # Extract substring of length len(t) from s 
        substring = s[i:i+len(t)]
        if substring == t:
            #append 1-based index
            loc.append(i +1) 
    return loc

string = "CTCGAGCACTCGAGCCTCGAGCGCTCGAGCCTCGCTCGAGCGCTCGAGCGCTCGAGCCTCGAGCCCTCGAGCCTCGAGCTACTCGAGCGCTCGAGCAATCTCGAGCTACTCGAGCTAGCGACTCGAGCCTCGAGCACTCGAGCTCCGCTCGAGCTCACTCGAGCCACCTCGAGCCTCTCGAGCCTCGAGCGCCTCGAGCAGAGATCTCGAGCACTCGAGCCTCGAGCCTCGAGCCTCGAGCCGAACTCGAGCGCTCGAGCAAGTCCTCGAGCTGCCAAACCACCCTCGAGCCCCAGCTGAGCTCGAGCGAACTCGAGCTATTCTGAAGGTCTCGAGCTCTCGAGCCAAACCTCGAGCCTCGAGCACTCGAGCCCGCTCGAGCCTCGAGCGGTTACTCGAGCCTCGAGCCTCGAGCTACTCGAGCGTCTCGAGCCTCGAGCGGTCTCGAGCACGGCCTCGAGCCCCCTCGAGCGCTCGAGCCTCGAGCAAGTCGCTCGAGCGCTCGAGCCATTTACTCGAGCCTCGAGCGGATTCCTCGAGCAGCGCCTCGAGCCTCGAGCCATCTCGAGCCTCGAGCTCTCGAGCCCTCGAGCCGCTCGAGCCGCCTTTGGTATTTATAGCTCGAGCGTGCTCGAGCTCTCGAGCTCCCCTCGAGCCCAACTGGATATGCCCGCGACTCGAGCCTCGAGCACCCGGTCTCGAGCATTCTCGAGCGCGAGGCGGAAAGCTCGAGCCTCGAGCACTTCCTCGAGCCTCGAGCTTCCTCGAGCCTCGAGCTCTCGAGCTGGCTCGAGCCTCGAGCTCGCTCGAGCATCTCGAGCTCTCGAGCACTCGAGCCTCGAGCGGTACTCGAGCAGATTCTCGAGCCCTCGAGCGCCTCGAGCGCTCGAGCGAACTCGAGCGAGAATTAACATCTCGAGCTCCCTCGAGCCTCGAGCCTCGAGC"

substring = "CTCGAGCCT"

result = FindingMotif(string, substring)

for i in result:
    print(i)