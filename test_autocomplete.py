"""
This file is to learn how to use pytest.
"""


# https://www.codewars.com/kata/5389864ec72ce03383000484/train/python
import pytest
import os

def autocomplete(input_, dictionary):
    #your code here
    result = []
    for d in dictionary:
        if d.find(input_) == 0:
            result.append(d)
            
    return result


def test_autocomplete():
	dictionary = ['abnormal', 'arm-wrestling', 'absolute', \
	'airplane', 'airport', 'amazing', \
	'apple', 'ball']

	assert autocomplete('ai', dictionary) == ['airplane','airport']
	# assert autocomplete('a', dictionary) == ['abnormal','arm-wrestling','absolute','airplane','airport']


if __name__ == '__main__':
	os.system("pytest")