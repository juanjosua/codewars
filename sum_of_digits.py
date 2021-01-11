def sum(number):
    result = 0
    for n in str(number):
        result += int(n)

    if len(str(result)) > 1:
        sum(result)
    else:
        print(result)


sum(16)  # 1 + 6 = 7
sum(1234)  # 1 + 2 + 3 + 4 = 10, 1 + 0 = 1
