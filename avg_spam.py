###################################################################
### Program that opens file, reads it line by line, extracts    ###
### the given spam confidence data from it and calculates       ###
### the average spam confidence from the extracted data.        ###
### Assignment for 'Programming for Everybody' course on        ###
### Coursera offered by University of Michigan                  ###
### https://www.coursera.org/course/pythonlearn                 ###
###################################################################

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

count = 0
total_spam = float(0)

# loops through the lines and extracts spam confidence from relevant lines
fh = open(fname)
for line in fh:    
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    spam = float(line[19:])
    total_spam = total_spam + spam

# calculates and prints the average spam confidence
avg_spam = total_spam / float(count)
print "Average spam confidence: %0.12f" % avg_spam