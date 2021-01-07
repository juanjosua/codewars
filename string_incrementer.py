""" 
Instructions :
Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

link: https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

"""


def increment_string(string):
    s = ''.join(x for x in string if x.isdigit())
    if s == []:
        print(string + str('1'))
    else:
        print(int(s))
    # print(num)


# Voted as best practice
def count2(string):
    return {i: string.count(i) for i in string}


# increment_string('foo')  # foo1
increment_string('foo01')  # foo2
