"""
Instructions :
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

mahouka koukou no rettousei
misfit of demon king academy

"""


# My code
def duplicate_count(text):
    # Your code goes here
    txt = str(text).lower()
    counter = dict.fromkeys(txt, 0)
    result = 0
    for t in txt:
        counter[t] += 1

    for key, val in counter.items():
        if val > 1:
            result += 1

    print(result)
    return result


# Voted as best practice
def duplicate_count2(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


duplicate_count("abcde")  # 0
duplicate_count("abcdea")  # 1
duplicate_count("indivisibility")  # 1
