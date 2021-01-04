"""
Instructions:
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

Link: https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

"""


def get_count(input_str):
    # your code here
    dict = {
        "a": 0,
        "i": 0,
        "u": 0,
        "e": 0,
        "o": 0
    }

    result = 0
    for i in input_str:
        if i in dict:
            dict["a"] += 1

    for key, value in dict.items():
        result += value

    print(result)
    return result


# Voted for best practices
def getCount2(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")


def getCount3(s):
    return sum(c in 'aeiou' for c in s)


get_count("abracadabra")  # 5
get_count("")  # 0
get_count("pear tree")  # 4
get_count("o a kak ushakov lil vo kashu kakao")  # 13
