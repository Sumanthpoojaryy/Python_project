class Student:
    def __init__(self, student_id, name, math, physics, chemistry, biology):
        self.student_id = student_id
        self.name = name
        self.math = int(math)
        self.physics = int(physics)
        self.chemistry = int(chemistry)
        self.biology = int(biology)
        self.average = (self.math + self.physics + self.chemistry + self.biology) / 4


def analyze_grades(input_file):

    students = []

    # Read file
    with open(input_file, "r") as file:
        lines = file.readlines()

    # Process lines (skip header)
    for line in lines[1:]:

        line = line.strip()

        if line == "":        # skip empty lines
            continue

        data = line.split(",")

        if len(data) != 6:    # skip incorrect format
            continue

        student = Student(
            data[0],
            data[1],
            data[2],
            data[3],
            data[4],
            data[5]
        )

        students.append(student)

    total_students = len(students)

    if total_students == 0:
        print("No valid student data found.")
        return

    # Subject totals
    math_total = physics_total = chemistry_total = biology_total = 0

    math_scores = []
    physics_scores = []
    chemistry_scores = []
    biology_scores = []

    for s in students:
        math_total += s.math
        physics_total += s.physics
        chemistry_total += s.chemistry
        biology_total += s.biology

        math_scores.append(s.math)
        physics_scores.append(s.physics)
        chemistry_scores.append(s.chemistry)
        biology_scores.append(s.biology)

    # Subject averages
    math_avg = math_total / total_students
    physics_avg = physics_total / total_students
    chemistry_avg = chemistry_total / total_students
    biology_avg = biology_total / total_students

    # Overall average
    overall_avg = sum(s.average for s in students) / total_students

    # Top 3 students
    students.sort(key=lambda x: x.average, reverse=True)
    top_3 = students[:3]

    # Students scoring above 90
    above_90 = []
    for s in students:
        if s.math > 90 or s.physics > 90 or s.chemistry > 90 or s.biology > 90:
            above_90.append(s)

    # ===== PRINT REPORT =====
    print("\n===== STUDENT PERFORMANCE REPORT =====\n")

    print("Total Students:", total_students)

    print("\nClass Average Per Subject:")
    print("Math:", round(math_avg, 2))
    print("Physics:", round(physics_avg, 2))
    print("Chemistry:", round(chemistry_avg, 2))
    print("Biology:", round(biology_avg, 2))

    print("\nOverall Class Average:", round(overall_avg, 2))

    print("\nTop 3 Students:")
    for s in top_3:
        print(s.name, "-", round(s.average, 2))

    print("\nStudents Scoring Above 90 in Any Subject:")
    for s in above_90:
        print(s.name)

    print("\nSubject-wise Highest and Lowest Scores:")
    print("Math - Highest:", max(math_scores), "Lowest:", min(math_scores))
    print("Physics - Highest:", max(physics_scores), "Lowest:", min(physics_scores))
    print("Chemistry - Highest:", max(chemistry_scores), "Lowest:", min(chemistry_scores))
    print("Biology - Highest:", max(biology_scores), "Lowest:", min(biology_scores))


# Call function
analyze_grades("student.txt")

