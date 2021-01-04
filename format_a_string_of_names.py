"""
Instructions:
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.

Link: https://www.codewars.com/kata/53368a47e38700bd8300030d/train/python

"""


def namelist(names):
    # your code here
    result = ''
    if len(names) != 0:
        arr = []
        for i in range(0, len(names) - 1):
            arr.append(names[i]['name'])

        result = ', '.join(arr)
        if result != '':
            result += ' & ' + names[len(names) - 1]['name']
        else:
            result = names[-1]['name']

    print(result)
    return result


# Voted for best practices
def namelist2(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
namelist([{'name': 'Bart'}, {'name': 'Lisa'}])
namelist([{'name': 'Bart'}])
namelist([])
