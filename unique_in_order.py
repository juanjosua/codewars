""" 
Instructions :
Implement the function unique_in_order which takes as argument a sequence and returns a list of items 
without any elements with the same value next to each other and preserving the original order of elements.

For example:
unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

link: https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

"""


def unique_in_order(iterable):
    result = []
    for i in iterable:
        if len(result) == 0 or result[-1] != i:
            result.append(i)

    print(result)
    return result


# Voted as best practice
def unique_in_order2(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


unique_in_order('AAAABBBCCDAABBB')  # ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')  # ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])  # [1, 2, 3]
