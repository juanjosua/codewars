"""
TWO SUM

LINK: https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple like so: (index1, index2).
For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

"""

def two_sum(numbers, target):
    # start coding!
    result = []
    for i, v in enumerate(numbers):
    	tmp = target - v
    	if tmp in numbers:
    		result.append(i)
    		result.append(len(numbers) - numbers[::-1].index(tmp) - 1)
    		break

    print(result)

# voted best practice
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]

# test code
two_sum([1,2,3], 4) #[0, 2]
two_sum([2,2,3], 4) #[0, 1]