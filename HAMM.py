#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:43:32 2024
Given two strings s and t of equal length, the Hamming distance between s and t,
 denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
 See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
@author: sofiyapatra
"""

def HammingDistance(s: str, t: str) -> int:
    #initialize distance
    distance=0
    #iterate along length of sequence 1 
    for i in range(len(s)): 
        #check if the nucleotide of sequence 1 matches the nucleotide of sequence 
        #2 at the same index 
        if s[i] != t[i]:
            #update distance 
            distance += 1 
    return distance

s= 'GAGACTCTAGCTAAAGGTCTTACGTAAAATGGTCTGGCCAAGCCTAGGAAATTGGCTGTAGCAGGTGCGGCGACAACCGGTTAGTTATGTTATATTCGGACCTCGGCTCGAAAAGGAAGGTGAGAGCTATTGCATACCCGGTCTCTATGAACACGTTTCCTCGAATACGTATTACCCCATGTATCCTCGTTTCCCTTGCTACTAATCCCTATTGCCTGTTAACCTCGATAGTGATCCTGTATGACCCAGTCTCCAAGGTCGGGTGAGGTAAGCACAATGAGGAGACCCTCGTACGTTGCCCTCACTTAAATAGGGGCGGTTGGAGGAGGGTACCTGGTTTACACAAGCCAGAGCGCTTAGTAAATACTAGTAGAGCCGTACCACCATAAGAAACCCGGTACCCTGAGTATCATGTGAAGTGGGATACCGGTTATGCGCAGGTAGCGTACCTTCTTAGTTCCAAAACAAAGGGACGGCCCGGGATTAGCTGTAATCTCGAACCTTTCAACCGGCTTAGTCACATGTGCCACACCCACGTAGATCGCGCAATTTCAGCCACACGTACCAATGCACCCGCTTTTCAATAGTGGATGGGCGTAGTGCCCGCCATCGGCCGGTATTGATGTGCTCATCTCCACCCCCGCACCAACCAAGTGTTCCGTACTATGCTGCTGGCCCCAGTGTCGCACTCAGCGCGCAGGATTCCATTTCTCCTGAGCCACCAGGCACCCACTCGGGCGCTCCCCGAGCTATTTCTTATGTGAATCCATCCAGCTACGCTTTTCCTCGAAATTACACTTAATAACCCACCTAACCCCCCACTCATACCATTCTCAGTGTTAACATGGGATGCATTCGTTGTCGATAGAAAGTCTCCAGTTTCGCCCGGAACACATGCTGTGTATTATAGATCTCCTTGTCCACAAATGGTATTCCGGGACCATTCAACTTTTGTATAGA'
t = 'GAAACGGTCGCGGACGCTCTGACCTCCAGCCGTCTTGTAAGGCATAAGAGGCTGTCTTCAGGTGTGGGGGCATGAGGCACCTCGTTATAAGAGCATACCACCTAAACGTTTGAAGGAAGGCAAGAGTTAACTGCTATCCGGTTCATAGGAGGCGCTTTACTAGAATACCGTGCTTTCCAAGCACTCCCGTAGGCCAGTCTACTAATCCTTTTGGCTGGCCAAAGTGAGTACGAGACAGCAGTGACTAAATCTCAATGTCGGGAGGTTGTTTCCGACCTTGATAGCCCTCTGTAGTTTCCCGAAAAATAAATAGTGATGGTTGGAAATGGAGATCGGGAATATTGAAGTTACCACGTTCAAGAAAGGTCAACCGTATCCTCAAGGCCTAATTTAGCTAGTACCGAGGGGAAGAGCGGAGCGTAGATCCCCTGATTGAGCACATTGCGTGCCTTTTGGATTCATATACAAATAGGTGGTTGATGACTGGGGTGAATCTCGAGGCCTTGAACCAGCTAATAGACATGTGGAAGCCATATCTAAATACTTCAATCTCGGCGACCCGTATCACTGCGTTCATCTTCCTAGTTGAGGTGGTCAGGCGTTCTGCCATGGTGCGGGGCTGGTGCCCTTTCCACTAGACCCACGCAAACCATTTAAGCGGCGCTATTCTGCAGAGCAACTTTTGCCATTCCTCTCCCCGGACACCGGCGACCCTGTACGAAAAGTCACGGTCACGGGTCCGTGCGGACATATGTGCTAAACACCCTCACCAGTTGAAGGTCGTCTTCCTCACTGCACCTTATGGCCCATATATTCCACCACTAAAGATAGGCTCGATCTTTTGCTTGGATTCCGCGGTGGGCCGTTGACACGACCCTTTGGCGCCCGGAAAACATGATTAGGACTTTATTCCTCCACGTATAGTGATGGTGTGGTGTTATCAGTCTATTATTGATCAGC'
HammingDistance(s, t)