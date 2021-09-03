# https://www.codewars.com/kata/5389864ec72ce03383000484/train/python
import re

def autocomplete(input_, dictionary):
    #your code here
    input_clean = re.sub('[^A-Za-z]+',  '', input_)    
    result = []
    for d in dictionary:
        if d.lower().find(input_clean) == 0:
            result.append(d)
            
    return result[:5]


if __name__ == '__main__':
	dictionary=[ 'abnormal',
  'arm-wrestling',
  'absolute',
  'airplane',
  'airport',
  'amazing',
  'apple',
  'ball' ]

	print(autocomplete('ai', dictionary))
	print(autocomplete('a', dictionary))