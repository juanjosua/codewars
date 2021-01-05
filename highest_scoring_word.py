"""
Instructions :
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.

link: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

"""


# My code
def high(sentence):
    # Code here
    words = sentence.split(' ')
    weight = {}
    for word in words:
        weight[word] = 0
        for char in word.lower():
            weight[word] += ord(char)
            print([char, ord(char)])

    winner = max(weight, key=weight.get)
    # print(weight)
    # print(winner)
    return winner


# Voted as best practice
def sort_array2(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


high('abcdefghijklmnopqrstuvwxyz')  # ubud
# high('man i need a taxi up to ubud')  # ubud
# high('what time are we climbing up the volcano')  # volcano
# high('take me to semynak')  # semynyak
