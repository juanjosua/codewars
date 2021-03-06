""" 
Instructions :
Given two integers a and b, which can be positive or negative, find the sum of all the integers between including them too and return it. If the two numbers are equal return a or b.
Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

link: https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

"""


# My code
def get_sum(a, b):
    # good luck!
    res = 0

    if a > b:
        start = b
        end = a
    else:
        start = a
        end = b

    for i in range(start, end + 1):
        res += i

    print(res)
    return res


# Voted as best practice
def get_sum2(a, b):
    return sum(range(min(a, b), max(a, b)+1))


get_sum(1, 0)  # 1
get_sum(1, 2)  # 3
get_sum(0, 1)  # 1
get_sum(1, 1)  # 1
get_sum(-1, 0)  # -1
get_sum(-1, 2)  # 2
