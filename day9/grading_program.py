# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the
# names of the students and the values are their exam scores.
#
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary
# called student_grades that should contain student names for keys and their grades for values. The final version of
# the student_grades dictionary will be checked.
#
# DO NOT write any print statements.
#
# These are the scoring criteria:
#
#     Scores 91 - 100: Grade = "Outstanding"
#
#     Scores 81 - 90: Grade = "Exceeds Expectations"
#
#     Scores 71 - 80: Grade = "Acceptable"
#
#     Scores 70 or lower: Grade = "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

for student in student_scores:
    if student_scores[student] > 90:
        print(f'{student}, you are Outstanding.')
    elif 90 > student_scores[student] > 80:
        print(f'{student}, you are Above average.')
    elif 80 > student_scores[student] > 70:
        print(f'{student}, you are Average af.')
    else:
        print(f'{student}, you dumb as hell lmao.')

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = 'A'
    elif 90 > student_scores[student] > 80:
        student_grades[student] = 'B'
    elif 80 > student_scores[student] > 70:
        student_grades[student] = 'C'

print(student_grades)
