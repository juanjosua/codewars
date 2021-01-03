""" 
Instructions :
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case 

link: https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

"""

# My code


def is_isogram(string):
    # your code here
    counter = {}
    result = 'True'
    string = string.lower()

    for letter in string:
        if letter in counter:
            counter[letter] += 1
            result = 'False'
        else:
            counter[letter] = 1

    if result == 'True':
        print(result)
        return True
    else:
        print(result)
        return False


# Voted as best practice
def is_isogram2(string):
    return len(string) == len(set(string.lower()))


is_isogram("Dermatoglyphics")
is_isogram("aba")
is_isogram("moOse")
