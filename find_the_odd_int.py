"""
Find the Odd Int
LINK: https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

"""

def find_it(seq):
	numbers = set(seq)
	return[n for n in numbers if seq.count(n) % 2 ==1][0]

# voted best practice 1
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]

# voted best practice 2
def find_it(seq):
	for i in seq:
	    if seq.count(i)%2!=0:
	        return i

# test code
find_it([10]) #10
find_it([1,1,1,2,2]) #1