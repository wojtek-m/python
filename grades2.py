####################################################
### Exam grading exercise.                       ###
### Exercises from Codecademy Python track.      ###
### http://www.codecademy.com/en/tracks/python   ###
####################################################

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

""" Prints a list of all grades """
def print_grades(grades):
    for grade in grades:
        print grade

""" Calculates the sum of all grades """
def grades_sum(grades):
    total = 0
    for grade in grades:
        total = total + grade
    return total

""" Calculates the average of all grades """
def grades_average(grades):
    average = grades_sum(grades) / float(len(grades))
    return average

""" Calculates the variance for all grades """
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance = variance / float(len(scores))
    return variance

""" Calculates the standard deviation for all grades"""
def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)

print "List of grades: "    
print_grades(grades)
print "Grades sum: %s" % grades_sum(grades)
print "Grades average: %s" % grades_average(grades)
print "Grades Variance: %s" % grades_variance(grades)
print "Grades Standard Deviation: %s" % grades_std_deviation(variance)