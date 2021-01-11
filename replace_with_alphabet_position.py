""" 
Instructions :
In this kata you are required to, given a string, replace every letter with its position in the alphabet.
If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Examples:

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

link: https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

"""

import re


def alphabet_position(text):
    text = re.sub(r'[^\w]', ' ', text).lower()
    print(' '.join([str(ord(t) - 96) for t in text if t != ' ']))


# Voted as best practice
def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


alphabet_position("The sunset sets at twelve o' clock.")
alphabet_position("The narwhal bacons at midnight.")
