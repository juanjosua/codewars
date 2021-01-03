""" 
Instructions :
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. 
Bob observed that one number usually differs from the others in evenness. 

Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

link: https://www.codewars.com/kata/552c028c030765286c00007d/train/python

"""


def iq_test(numbers):
    num_split = numbers.split(" ")
    num_int = [int(n) for n in num_split]

    mod_counter_even = 0
    mod_counter_odd = 0
    counter = 1

    for n in num_int:
        if n % 2 == 0:
            mod_counter_even += 1
        else:
            mod_counter_odd += 1

    for n in num_int:
        if mod_counter_even > mod_counter_odd and n % 2 != 0:
            print(counter)
            return counter
        elif mod_counter_odd > mod_counter_even and n % 2 == 0:
            print(counter)
            return counter
        counter += 1


# Voted as best practice
def iq_test2(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


iq_test("2 4 7 8 10")
iq_test("1 2 1 1")
