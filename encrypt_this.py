"""
Encrypt this
LINK: https://www.codewars.com/kata/5848565e273af816fb000449/train/python

Description:

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

    1. Your message is a string containing space separated words.
    2. You need to encrypt each word in the message using the following rules:
       - The first letter needs to be converted to its ASCII code.
       - The second letter needs to be switched with the last letter
    3. Keepin' it simple: There are no special characters in input.

examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"

"""

def encrypt_this(text):
	leng = len(text)
	words = text.split(' ')
	result = []
	if leng > 1:
		for w in words:
			word = list(w)
			word[0] = str(ord(w[0]))
			word[1], word[-1] = word[-1], word[1]
			word = ''.join(word)
			result.append(word)

		print(' '.join(result))
	elif leng == 1:
		print(str(ord(text)))
	else:
		print(text)

# voted best practice 

# test code
encrypt_this("Hello")
encrypt_this("good")
encrypt_this("hello world")
encrypt_this("A")
encrypt_this("")