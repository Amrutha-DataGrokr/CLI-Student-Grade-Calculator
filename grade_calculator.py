"""
CLI Student Grade Calculator
Reads student marks from a CSV file.
Calculates total, average, highest and lowest marks.
Assigns grades and determines pass/fail status.
Displays and saves the student grade report.
"""
import os
import csv
def load_students(path):
    try:
        with open(path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            required_columns = ["Name", "Math", "Science", "English", "History", "PE"]

            if not all(column in reader.fieldnames for column in required_columns):
                print("Error: CSV file is missing required columns.")
                return None
            students = []

            for row in reader:
                students.append(row)

            subjects = ["Math", "Science", "English", "History", "PE"]

            for student in students:
                for sub in subjects:
                    student[sub] = int(student[sub])

            return students

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return None

    except ValueError:
        print("Error: Invalid marks found. Marks must be numeric.")
        return None

def calculate_stats(scores):
    try:
        if not scores:
            raise ValueError("Scores list cannot be empty.")

        report = {}
        report["total"] = sum(scores)
        report["average"] = round(report["total"] / len(scores), 2)
        report["highest"] = max(scores)
        report["lowest"] = min(scores)

        if report["average"] >= 90:
            report["grade"] = 'A'
        elif report["average"] >= 80:
            report["grade"] = 'B'
        elif report["average"] >= 70:
            report["grade"] = 'C'
        elif report["average"] >= 60:
            report["grade"] = 'D'
        else:
            report["grade"] = 'F'

        return report

    except ValueError as e:
        print(f"Error: {e}")
        return None

def display_report(students):
    print("=" * 55)
    print(" " * 15 + "STUDENT GRADE REPORT")
    print("=" * 55)

    print(f"{'Name':<15}{'Average':<15}{'Grade':<12}{'Status'}")
    print("-" * 55)

    for student in students:
        scores = [value for key, value in student.items()if key != "Name"]

        report = calculate_stats(scores)
        if report is None:
            continue

        print(
            f"{student['Name']:<15}"
            f"{report['average']:<15.2f}"
            f"{report['grade']:<12}"
            f"{'Pass' if report['average'] >= 60 else 'Fail'}"
        )

    print("=" * 55)

def save_report(students, output_path):
    try:
        averages = []
        passed = 0
        failed = 0

        with open(output_path, mode="w") as file:
            file.write("=" * 55 + "\n")
            file.write(" " * 15 + "STUDENT GRADE REPORT\n")
            file.write("=" * 55 + "\n")
            file.write(f"{'Name':<15}{'Average':<15}{'Grade':<12}{'Status'}\n")
            file.write("-" * 55 + "\n")

            for student in students:
                scores = [value for key, value in student.items()if key != "Name"]
                report = calculate_stats(scores)
                if report is None:
                    continue
                average = report["average"]
                grade = report["grade"]
                status = "Pass" if average >= 60 else "Fail"
                averages.append(average)

                if status == "Pass":
                    passed += 1
                else:
                    failed += 1

                file.write(
                    f"{student['Name']:<15}"
                    f"{average:<15.2f}"
                    f"{grade:<12}"
                    f"{status}\n"
                )

            file.write("=" * 55 + "\n")
            if averages:
                class_average = sum(averages) / len(averages)
                file.write("\nCLASS SUMMARY\n")
                file.write("-" * 55 + "\n")
                file.write(f"Total Students: {len(averages)}\n")
                file.write(f"Class Average: {class_average:.2f}\n")
                file.write(f"Highest Average: {max(averages):.2f}\n")
                file.write(f"Lowest Average: {min(averages):.2f}\n")
                file.write(f"Students Passed: {passed}\n")
                file.write(f"Students Failed: {failed}\n")
                file.write("=" * 55 + "\n")

        print(f"Report successfully saved to '{output_path}'")

    except PermissionError:
        print("Error: Permission denied while writing the report.")

    except OSError as e:
        print(f"Error while saving report: {e}")

def main():
    try:
        input_path = input("Enter input file path (default: students_input.csv): ").strip()
        input_path = input_path or "students_input.csv"

        students = load_students(input_path)
    
        if students is not None:
            display_report(students)
            output_path = os.path.join(os.getcwd(), "grades_report.txt")
            save_report(students,output_path)
    except FileNotFoundError:
        print("Error: Input file not found.")

if __name__=="__main__":
    main()