#####################################################################
### Program that calculates student final grade based on weighted ###
### average of all course grades.                                 ###
### Exercise from Codeacademy.com Python track                    ###
### http://www.codecademy.com/en/tracks/python                    ###
#####################################################################


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = {
    "Lloyd" : lloyd,
    "Alice" : alice,
    "Tyler" : tyler,
}


# calculates the average grade
def average(numbers):
    total = float(sum(numbers))
    avg_score = total / len(numbers)
    return avg_score

# calculates the weighted average total score 
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    avg_grade = 0.1 * homework + 0.30 * quizzes + 0.60 * tests
    return avg_grade

# assigns the grade
def get_letter_grade(score):
    if score > 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# calculates the class average
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(students[student]))
    return average(results)

# prints the grade of the selected student and the class average
name = raw_input("Please enter student's name (Lloyd, Alice or Tyler): ")
final_grade = get_letter_grade(get_average(students[name]))
print "The final grade for %s was %s" % (name, final_grade)
print "The class average was %s" % (get_letter_grade(get_class_average(students)))