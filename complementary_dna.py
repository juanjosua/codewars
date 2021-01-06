"""
Instructions :
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
If you want to know more http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

Examples:
DNA_strand ("ATTGC") # return "TAACG"
DNA_strand ("GTAT") # return "CATA"

link: https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

"""


# My code
def DNA_strand2(dna):
    # code here
    result = ''
    for char in dna.upper():
        if char == 'A':
            result += 'T'
        elif char == 'T':
            result += 'A'
        elif char == 'G':
            result += 'C'
        else:
            result += 'G'

    print(result)
    return result


# Voted as best practice
def DNA_strand1(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


# Voted as best practice2
def DNA_strand(dna):
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([pairs[x] for x in dna])


DNA_strand("ATTGC")  # return "TAACG"
DNA_strand("GTAT")  # return "CATA"
