####################################################
### Functions practice.                          ###
### Exercises from Codecademy Python track.      ###
### http://www.codecademy.com/en/tracks/python   ###
####################################################

""" Function that sums the the digits of an inputed number """

def digit_sum(n):
    sum = 0
    i = 0
    str_num = str(n)
    for digit in range(0, (len(str_num))):
        sum = sum + int(str_num[digit])
    return sum


""" Function that removes vowels from input text """

def anti_vowel(text):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    no_vow_txt = ""
    for char in text:
        if char in vowels:
            continue
        else:
            no_vow_txt+=char
    return no_vow_txt


""" Function that returns a reversed input text """ 

def reverse(text):
    i = len(text) - 1
    reversed_txt = ""
    for char in text:
        reversed_txt+=(text[i])
        i -= 1
    return reversed_txt


""" Function that determines if a number is a prime """

def is_prime(x):
    if x < 2:
        return False
    else:
        for num in range(2, abs(x)-1):
            print "num: %s" % num
            print "modulo: " (abs(x) % num)
            if abs(x) % num == 0:
                return False
                break
        return True