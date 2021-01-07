""" 
Instructions :
Your goal in this kata is to implement a difference function, 
which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

link: https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

"""


def array_diff(a, b):
    # your code here
    res = []
    for i in a:
        if i in b:
            continue
        else:
            res.append(i)

    print(res)


# Voted as best practice
def array_diff2(a, b):
    return [x for x in a if x not in b]


array_diff([1, 2], [1])  # [2]
array_diff([1, 2, 2], [1])  # [2, 2]
