"""
Instructions :
The goal of this exercise is to convert a string to a new string where each character in the new string 
is "(" if that character appears only once in the original string, or ")" if that character appears 
more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples:
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("

Notes:
Assertion messages may be unclear about what they display in some languages. 
If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

"""


# My code
def duplicate_encode(word):
    # your code here
    result = ''
    low_word = word.lower()
    for char in low_word:
        count = low_word.count(char)
        if count > 1:
            result += ")"
        else:
            result += "("

    print(result)
    return result


# Voted as best practice
def duplicate_encode2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


duplicate_encode("din")  # "((("
duplicate_encode("recede")  # "()()()"
duplicate_encode("Success")  # ")())())"
duplicate_encode("(( @")  # "))(("
duplicate_encode("Supralapsarian")  # ")()))()))))()("
