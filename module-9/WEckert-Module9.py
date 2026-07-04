#======================================================================
#Title: Module 9.2 Assignment
#Author: Wade Eckert
#Date: 02 November 2025
#Description: This program create a student class that will calculate and display 
#student cumulative GPA. 
#======================================================================

#Create a student class that will calculate and display student cumulative GPA.
class Student: 
    
    #Define the __init__ method to initialize the attributes of the student class.
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__grade = 0
        self.__grade_point = 0
        self.__credits = 0
        self.__gpa = 0
      
    #Define the CalculateGPA method to calculate the student's cumulative GPA.
    def CalculateGPA(self, grade, credits):
        self.__grade += grade
        self.__credits += credits
        self.__grade_point += grade * credits
        self.__gpa = self.__grade_point / self.__credits
        return self.__gpa

    #Define the GetGPA method to return the student's cumulative GPA.
    def GetGPA(self):
        return self.__gpa

#Create a main function to prompt the user for the first and last name of the student.
def main():
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
  
    #Create a student object by passing the first and last name to the __init__ method.
    student = Student(first_name, last_name)

    #Create a loop that prompts the user for the credits and grade for each course of the student.
    course_number = 1
    while True:
        if course_number == 1:
            course_number_suffix = "st"
        elif course_number == 2:
            course_number_suffix = "nd"
        elif course_number == 3:
            course_number_suffix = "rd"
        else:
            course_number_suffix = "th"

        try:
            credits = int(input(f"\nEnter the credits for the {course_number}{course_number_suffix} "
                                f"course of {first_name} {last_name}: "))
        except ValueError:
            print("\nInvalid input. Please enter a number for credits.")
            continue

        grade = input(f"Enter the grade for the {course_number}{course_number_suffix} "
                     f"course of {first_name} {last_name} (A-F): ").upper()
        #Convert the grade to a number.
        if grade == 'A':
            grade = 4
        elif grade == "B+":
            grade = 3.5
        elif grade == 'B':
            grade = 3
        elif grade == "C+":
            grade = 2.5
        elif grade == 'C':
            grade = 2
        elif grade == 'D':
            grade = 1
        elif grade == 'F':
            grade = 0
        else:
            print("\nInvalid grade. Please enter a valid grade between A and F from the grading scale.") 
            continue
        course_number += 1

        #Calculate the student's cumulative GPA by calling the CalculateGPA method.
        student.CalculateGPA(grade, credits)
        
        #Ask the user if they want to enter another course.
        another = input("Do you want to enter another course? (y/n): ")
        if another.lower() != 'y':
            break
        
    #Once the user ends the loop, display the student’s cumulative GPA.
    print("\nStudent: ", first_name, last_name)
    print("The student's cumulative GPA is: ", student.GetGPA())
    
#Create a intro function to display the purpose of the program.
def intro():
    print("This program calculates a student's cumulative GPA.")
    print("It prompts for the student's name and course details (credits and letter grade).")
    print("The student's GPA is then displayed.")
    print("\nThe grading scale is:")
    print("A = 4.0, B+ = 3.5, B = 3.0, C+ = 2.5, C = 2.0, D = 1.0, F = 0\n")

#Call the intro function to display the purpose of the program.
intro()

#Call the main function to execute the program.
if __name__ == '__main__':
  main()