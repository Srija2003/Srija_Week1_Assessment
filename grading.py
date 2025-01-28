def get_student_name():
    return input("Enter the student's name: ")

def get_marks():
    
    marks = []
    print("Enter the marks for 5 subjects (out of 100):")
    for i in range(1, 6):
        mark = float(input(f"Subject {i}: "))
        while mark < 0 or mark > 100:
            print("Invalid marks. Please enter a value between 0 and 100.")
            mark = float(input(f"Subject {i}: "))
        marks.append(mark)
    return marks

def calculate_total(marks):
    """Calculates total marks."""
    return sum(marks)

def calculate_percentage(total_marks):
    """Calculates percentage."""
    return (total_marks / 500) * 100

def get_grade(percentage):
    """Determines grade based on percentage."""
    if percentage >= 85:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

def display_report(student_name, total_marks, percentage, grade):
    print("\n----- Student Grade Report -----")
    print(f"Student Name: {student_name}")
    print(f"Total Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

def main():
    
    student_name = get_student_name()
    marks = get_marks()
    total_marks = calculate_total(marks)
    percentage = calculate_percentage(total_marks)
    grade = get_grade(percentage)
    display_report(student_name, total_marks, percentage, grade)

# Run the program
main()