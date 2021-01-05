"""
Instructions :
You will be given an array of numbers.
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples:
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

link: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

"""


# My code
def sort_array(source_array):
    odd_list = [num for num in source_array if num % 2 == 1]
    sorted_odd_list = sorted(odd_list)

    for ind, val in enumerate(source_array):
        if val % 2 == 0:
            sorted_odd_list.insert(ind, val)

    print(sorted_odd_list)
    return sorted_odd_list


# Voted as best practice
def sort_array2(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


sort_array([5, 3, 2, 8, 1, 4])  # [1, 3, 2, 8, 5, 4]
sort_array([5, 3, 1, 8, 0])  # [1, 3, 5, 8, 0]
sort_array([2, 22, 37, 11, 4, 1, 5, 0])  # [2, 22, 1, 5, 4, 11, 37, 0]
sort_array([1, 111, 11, 11, 2, 1, 5, 0])  # [1, 1, 5, 11, 2, 11, 111, 0]
