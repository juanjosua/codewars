""" 
Instructions :
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.

link: https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

"""


def expanded_form(num):
    i = 10
    result = []
    while num > i / 10:
        number = int(num % i - num % (i / 10))
        if number > 0:
            result.append(number)
        i *= 10

    result.sort(reverse=True)
    print(' + '.join(str(i) for i in result))


# Voted as best practice
def expanded_form2(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y, x in enumerate(num) if x != '0')


expanded_form(12)  # Should return '10 + 2'
expanded_form(42)  # Should return '40 + 2'
expanded_form(70304)  # Should return '70000 + 300 + 4'
