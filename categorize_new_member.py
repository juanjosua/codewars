"""
Instructions :
The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
They would like your help with an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

Input :
Input will consist of a list of lists containing two items each. 
Each list contains information for a single potential member. 
Information consists of an integer for the person's age and an integer for the person's handicap.

Note for F#: The input will be of (int list list) which is a List<List>

Example input :
[[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]

Output :
Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

Example output :
["Open", "Open", "Senior", "Open", "Open", "Senior"]

link: https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

"""


def open_or_senior(data):
    array = []
    for d in data:
        if d[0] >= 55 and d[1] > 7:
            array.append('Senior')
        else:
            array.append('Open')
    print(array)
    return array


# Voted as best practice
def open_or_senior2(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for age, handicap in data]


open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])
open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)])
open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)])
