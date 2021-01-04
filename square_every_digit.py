"""
Instructions:
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

Link: https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

"""


def square_digits(num):
    num = str(num)
    result = ''

    for n in num:
        square = int(n)**2
        result = result + str(square)

    print(int(result))
    return int(result)


# Voted for best practices
def square_digits2(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)


square_digits(9119)  # 811181
square_digits(2112)  # 4114
