###################################################################
### Program that opens file, reads it line by line, extracts    ###
### e-mail addressed and prints the list and count of them.     ###
### Assignment for 'Programming for Everybody' course on        ###
### Coursera offered by University of Michigan                  ###
### https://www.coursera.org/course/pythonlearn                 ###
###################################################################

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

# loops through the file lines
for line in fh:
    line.rstrip()
    words = line.split()
    # conditions eliminating blank lines and unwanted lines
    if words == []:
        continue
    elif words[0] == "From:":
        continue
    elif words[0] != "From":
        continue
    # prints e-mail addresses
    else:
        print words[1]
        count = count + 1

# prints the count
print "There were", count, "lines in the file with From as the first word"
