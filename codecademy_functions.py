####################################################
### Functions practice.                          ###
### Exercises from Codecademy Python track.      ###
### http://www.codecademy.com/en/tracks/python   ###
####################################################

""" Function that takes two strings, text and word, as input and returns the text with 
the word you chose replaced with asterisks. """

def censor(text, word):
    text_list = text.split()
    ast_len = len(word)
    i = 0
    for wordlst in text_list:
        if text_list[i] == word:
            text_list[i] = ast_len * "*"
        i = i + 1
    censored_txt = " ".join(text_list)
    return censored_txt
        

""" Function that takes a string word and returns the equivalent scrabble score for that word. """

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word_low = word.lower()
    points = 0
    for char in word_low:
        if char in score:
            points = points + score[char]
    return points


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

""" Function that returns the number of times the item occurs in the list. """

def count(sequence, item):
    i = 0
    count = 0
    for element in sequence:
        if sequence[i] == item:
            count = count + 1
        i = i + 1
    return count

""" Function that takes in a list of numbers, removes all odd numbers in the list, and returns the result. """

def purify(numlist):
    i = 0
    new_list = []
    for item in numlist:
        if numlist[i] % 2 == 0:
            new_list.append(numlist[i]) 
        i = i + 1
    return new_list

""" Function that takes a list of integers as input and returns multiplication of all of the elements in the list. """ 

def product(numlist):
    total = 1
    i = 0
    for num in numlist:
        total = total * numlist[i]
        i = i + 1
    return total

""" Function that takes in a list and removes elements of the list that are the same."""

def remove_duplicates(numlist):
    unique_nums = []
    i = 0
    for num in numlist:
        if numlist[i] not in unique_nums:
            unique_nums.append(numlist[i])
        i = i + 1
    return unique_nums

""" Function that takes a list as an input and returns the median value of the list. """

def median(numlist):
    median = 0
    sortlist = sorted(numlist)
    if len(numlist) % 2 != 0:
        median = sortlist[int(len(sortlist)/2)]
    else:
        median = float((sortlist[(len(sortlist)/2)] + sortlist[(len(sortlist)/2) - 1]) / 2.0)
    return median
