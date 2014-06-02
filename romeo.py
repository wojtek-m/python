###################################################################
### Program that opens file, reads it line by line, adds unique ###
### words to the list and finally prints the sorted list of all ###
### unique words included in the textself.                      ###
### Assignment for 'Programming for Everybody' course on        ###
### Coursera offered by University of Michigan                  ###
### https://www.coursera.org/course/pythonlearn                 ###
###################################################################

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

# loops through all the lines and splits them into words
for line in fh:
    line.rstrip()
    words = line.split()
    # loops throught all the words in the line and adds unique words to the list
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)

# prints sorted list
list_alph = sorted(lst)
print list_alph