# Task 1: Student Class & Constructor

class Student:
    def __init__(self, name, roll_number, grades) :
        self.name = name
        self.roll_number = roll_number
        self.grades = grades
        
    # Task 2: Calculate GPA
  
    def calculate_gpa(self) :
        return sum(self.grades) / len(self.grades)

    # Task 2: Display Student Profile
  
    def display_profile(self) :
        print("----- Student Profile -----")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("GPA:", self.calculate_gpa())

    # Task 3: __str__ Dunder Method
  
    def __str__(self) :
        return f"Name: {self.name}, Roll Number: {self.roll_number}"


# Task 3: Create Student Objects

student1 = Student("Bisma", "101", [90, 85, 88])
student2 = Student("Zainab", "104", [78, 82, 80])
student3 = Student("Ayesha", "108", [95, 91, 93])


# Print Objects (__str__ Method)

print(student1)
print(student2)
print(student3)


# Display Student Profiles

student1.display_profile()
student2.display_profile()
student3.display_profile()
