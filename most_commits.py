###############################################################################################
### Program that reads through the mbox-short.txt and figures out who has the most commits. ###
### The program looks for 'From ' lines and takes the second word of those lines as the     ###
### person who sent the mail. The program creates a Python dictionary that maps the senders ###
### mail address to a count of the number of times they appear in the file.                 ###
### After the dictionary is produced, the program reads through the dictionary using        ###
### a maximum loop to find the most prolific committer.                                     ###
### Assignment for 'Programming for Everybody' course on Coursera offered by                ###
### University of Michigan. https://www.coursera.org/course/pythonlearn                     ###
###############################################################################################

name = raw_input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
committers = dict()

for line in handle:
    # eliminates the lines not starting with "From "
    if not line.startswith("From "): 
        continue
    # split the lines and appends the e-mails to a dictionary
    else:
        words = line.split()    
        committers[words[1]] = committers.get(words[1],0) + 1

most_commits = None
top_committer = None
# iterates through the dictionary and finds the top commiter
for committer, commits in committers.items():
    if most_commits is None or commits > most_commits:
        most_commits = commits
        top_committer = committer

print "The top commiter was " + top_committer + " with" " %s" % most_commits + " commits."
