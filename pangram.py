# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
import string
import re

def is_pangram(s):
    input_clean = re.sub('[^a-z]+',  '', s.lower())
    if len(set(input_clean)) == 26:
    	return True
    else:
    	return False


if __name__ == '__main__':
	pangram = "The quick, brown fox jumps over the lazy dog!"
	print(is_pangram(pangram))