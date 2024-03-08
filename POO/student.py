class Student:
    """
    A class representing a student.

    Attributes:
        name (str): The name of the student.
        age (int): The age of the student.
        grade (int): The grade of the student.
    """

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_grade(self, grade):
        self.grade = grade

    def __call__(self):
        """
        Call the student object, prints out the name, age, and grade.
        """
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


# Create multiple students
student1 = Student("John", 18, "A")
student2 = Student("Jane", 17, "B")
student3 = Student("Mike", 19, "C")

# Create an array to store the students
students: list[Student] = [student1, student2, student3]

# Add the new students to the students array
students.extend(
    [
        Student("Alice", 20, "A"),
        Student("Bob", 19, "B"),
        Student("Emily", 18, "C"),
        Student("David", 17, "A"),
        Student("Olivia", 19, "B"),
        Student("James", 20, "C"),
        Student("Sophia", 18, "A"),
        Student("Daniel", 17, "B"),
        Student("Isabella", 19, "C"),
        Student("William", 20, "A"),
        Student("Mia", 18, "B"),
        Student("Benjamin", 17, "C"),
        Student("Ava", 19, "A"),
        Student("Henry", 20, "B"),
        Student("Charlotte", 18, "C"),
        Student("Alexander", 17, "A"),
        Student("Amelia", 19, "B"),
        Student("Michael", 20, "C"),
        Student("Evelyn", 18, "A"),
        Student("Joseph", 17, "B"),
        Student("Harper", 19, "C"),
        Student("Daniel", 20, "A"),
        Student("Sophia", 18, "B"),
        Student("Matthew", 17, "C"),
        Student("Abigail", 19, "A"),
        Student("David", 20, "B"),
        Student("Emily", 18, "C"),
    ]
)

# Iterate over the students array and call the "call" method for each student
print([s() for s in students])
