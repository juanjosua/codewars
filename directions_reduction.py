# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python
def dirReduc(arr):
	if len(arr) == len(set(arr)):
		return arr

	result = []
	for a in arr:
		if len(result) == 0:
			result.append(a)
		else:
			if result[-1] == "NORTH" and a == "SOUTH":
				del result[-1]
			elif result[-1] == "SOUTH" and a == "NORTH":
				del result[-1]
			elif result[-1] == "WEST" and a == "EAST":
				del result[-1]
			elif result[-1] == "EAST" and a == "WEST":
				del result[-1]
			else:
				result.append(a)

	return result


if __name__ == '__main__':
	a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
	print(dirReduc(a)) # ['WEST']

	u = ["NORTH", "WEST", "SOUTH", "EAST"]
	print(dirReduc(u)) # ["NORTH", "WEST", "SOUTH", "EAST"]