# Existing student_scores dictionary (do not modify)
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Empty dictionary to store the grades
student_grades = {}

# Function to determine grade based on score
def convert_score_to_grade(score):
    if 91 <= score <= 100:
        return "Outstanding"
    elif 81 <= score <= 90:
        return "Exceeds Expectations"
    elif 71 <= score <= 80:
        return "Acceptable"
    else:
        return "Fail"

# Populating student_grades with names and assessed grades
for student, score in student_scores.items():
    student_grades[student] = convert_score_to_grade(score)

# Print the final student_grades dictionary to check the output
print(student_grades)
