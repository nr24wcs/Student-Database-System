class Student:
    def __init__(self, name, age, grades):
        """Initialize the student with a name, age, and a list of grades."""
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        """Display the student's name and age."""
        print(f"Name: {self.name}, Age: {self.age}")

    def calculate_average_grade(self):
        """Calculate and return the average grade of the student."""
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


def add_student():
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grades = list(map(int, input("Enter the student's grades separated by spaces: ").split()))
    return Student(name, age, grades)


student1 = Student("Taylor Swift", 20, [85, 90, 78])
student2 = Student("Travis Kelce", 22, [92, 88, 84, 79])
student3 = Student("Nathi", 19, [75, 80, 85, 70])


students = [student1, student2, student3]
add_more = input("Do you want to add a new student? (yes/no): ").strip().lower()

while add_more == 'yes':
    new_student = add_student()
    students.append(new_student)
    add_more = input("Do you want to add another student? (yes/no): ").strip().lower()


print("\nDisplaying all student information:\n")
for student in students:
    student.display_info()
    average_grade = student.calculate_average_grade()
    print(f"Average Grade: {average_grade:.2f}\n")
