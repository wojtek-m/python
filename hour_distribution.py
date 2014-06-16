###############################################################################################
### Program that reads through the mbox-short.txt and figures out the distribution by hour  ###
### of the day for each of the messages.                                                    ###
### Assignment for 'Programming for Everybody' course on Coursera offered by                ###
### University of Michigan. https://www.coursera.org/course/pythonlearn                     ###
###############################################################################################

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = dict()

for line in handle:    
    if not line.startswith("From") : continue
    words = line.split()
    for word in words:
        if len(word) < 3:
            continue
        elif word[2] == ":":
            hours[word[0:2]] = hours.get(word[0:2],0) + 1

hours_sorted = list()

for hour, count in hours.items():
    hours_sorted.append( (hour, count) )

hours_sorted.sort()

for hour, count in hours_sorted:
    print "Hour: %s / messages: %s" % (hour, count)

