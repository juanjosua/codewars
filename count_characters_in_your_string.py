""" 
Instructions :
The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

link: https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

"""


def count(string):
    # The function code should be here
    result = dict.fromkeys(string, 0)
    for s in string:
        result[s] += 1

    print(result)


# Voted as best practice
def count2(string):
    return {i: string.count(i) for i in string}


count('aba')  # {'a': 2, 'b': 1}
count('')  # {}
