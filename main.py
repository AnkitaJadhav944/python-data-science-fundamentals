"""
Module 01 Mini Project: Student Performance Analyzer
Concepts: variables, lists, dictionaries, loops, functions, and CSV file handling.
Run: python main.py
"""

import csv

DATA_FILE = "student_scores.csv"


def load_students(filename):
    """Read student records from a CSV file and return a list of dictionaries."""
    students = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["score"] = float(row["score"])
                students.append(row)
    except FileNotFoundError:
        print(f"Could not find {filename}. Keep it in the same folder as main.py.")
    return students


def calculate_average(students):
    """Calculate the class average."""
    if not students:
        return 0
    total = 0
    for student in students:
        total += student["score"]
    return total / len(students)


def find_topper(students):
    """Return the student with the highest score."""
    if not students:
        return None
    return max(students, key=lambda student: student["score"])


def count_results(students):
    """Count how many students passed (score >= 40) and need improvement."""
    passed = 0
    needs_improvement = 0
    for student in students:
        if student["score"] >= 40:
            passed += 1
        else:
            needs_improvement += 1
    return passed, needs_improvement


def save_report(students, average, passed, needs_improvement):
    """Write a simple summary report to a text file."""
    with open("performance_report.txt", mode="w", encoding="utf-8") as file:
        file.write("STUDENT PERFORMANCE REPORT\n")
        file.write("==========================\n")
        file.write(f"Number of students: {len(students)}\n")
        file.write(f"Class average: {average:.2f}\n")
        file.write(f"Passed: {passed}\n")
        file.write(f"Needs improvement: {needs_improvement}\n")
        topper = find_topper(students)
        if topper:
            file.write(f"Top performer: {topper['name']} ({topper['score']:.1f})\n")


def main():
    students = load_students(DATA_FILE)

    if not students:
        print("No student data available.")
        return

    average = calculate_average(students)
    topper = find_topper(students)
    passed, needs_improvement = count_results(students)

    print("\n===== STUDENT PERFORMANCE ANALYZER =====")
    print(f"Students analyzed: {len(students)}")
    print(f"Class average: {average:.2f}")
    print(f"Top performer: {topper['name']} ({topper['score']:.1f})")
    print(f"Passed: {passed}")
    print(f"Needs improvement: {needs_improvement}")

    print("\nIndividual scores:")
    for student in students:
        status = "Pass" if student["score"] >= 40 else "Needs improvement"
        print(f"- {student['name']}: {student['score']:.1f} | {status}")

    save_report(students, average, passed, needs_improvement)
    print("\nReport saved as performance_report.txt")


if __name__ == "__main__":
    main()
