""" 
Instructions :
This time no story, no theory. The examples below show you how to write function accum:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

link: https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

"""


def accum(string):
    # your code
    result = ''
    index = 0

    for letter in string:
        index += 1
        if index == len(string):
            result = result + (letter * index).capitalize()
        else:
            result = result + (letter * index).capitalize() + '-'

    print(result)
    return result


# Voted as best practice
def accum2(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


accum("abcd")
accum("RqaEzty")
accum("cwAt")
accum("equhxoswche")
