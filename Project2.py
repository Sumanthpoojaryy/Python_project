import csv

class Student:
    def __init__(self, student_id, name, math, physics, chemistry, biology):
        self.student_id = student_id
        self.name = name
        self.math = int(math)
        self.physics = int(physics)
        self.chemistry = int(chemistry)
        self.biology = int(biology)
        self.average = self.calculate_average()

    def calculate_average(self):
        return (self.math + self.physics + self.chemistry + self.biology) / 4


def analyze_grades(input_file, output_file):
    students = []

    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(
                    row['StudentID'],
                    row['Name'],
                    row['Math'],
                    row['Physics'],
                    row['Chemistry'],
                    row['Biology']
                )
                students.append(student)

    except FileNotFoundError:
        print("Error: Input file not found.")
        return

    total_students = len(students)

    # Subject-wise calculations
    subjects = ['math', 'physics', 'chemistry', 'biology']
    subject_totals = {sub: 0 for sub in subjects}
    subject_scores = {sub: [] for sub in subjects}

    for student in students:
        for sub in subjects:
            score = getattr(student, sub)
            subject_totals[sub] += score
            subject_scores[sub].append(score)

    subject_averages = {sub: subject_totals[sub]/total_students for sub in subjects}
    overall_class_average = sum([s.average for s in students]) / total_students

    # Top 3 students
    top_3 = sorted(students, key=lambda x: x.average, reverse=True)[:3]

    # Students scoring above 90 in any subject
    above_90_students = [
        s for s in students
        if s.math > 90 or s.physics > 90 or s.chemistry > 90 or s.biology > 90
    ]

    # Write Report
    with open(output_file, 'w') as report:
        report.write("===== STUDENT PERFORMANCE REPORT =====\n\n")
        report.write(f"Total Students: {total_students}\n\n")

        report.write("Class Average Per Subject:\n")
        for sub in subjects:
            report.write(f"{sub.capitalize()}: {subject_averages[sub]:.2f}\n")

        report.write(f"\nOverall Class Average: {overall_class_average:.2f}\n\n")

        report.write("Top 3 Students:\n")
        for student in top_3:
            report.write(f"{student.name} - {student.average:.2f}\n")

        report.write("\nStudents Scoring Above 90 in Any Subject:\n")
        for student in above_90_students:
            report.write(f"{student.name}\n")

        report.write("\nSubject-wise Highest and Lowest Scores:\n")
        for sub in subjects:
            report.write(
                f"{sub.capitalize()} - Highest: {max(subject_scores[sub])}, "
                f"Lowest: {min(subject_scores[sub])}\n"
            )

    print("Report generated successfully!")


analyze_grades("students.csv", "report.txt")
