#===================================================================
#Title: Module 2.2 Assignment
#Author: Wade Eckert
#Date: 15 September 2025
#Description: This program demonstrates a simple calculator
#for calculating the cost of installing fiber optic cable for
#a fictitious company based on the amount of feet the user enters. 
#This program demonstrates the print, input, and float
#functions, IF-ELIF-ELSE statements and variable assignment statements.
#===================================================================

#Make named constants for the cost per foot depending on the number of feet.
no_discount = .87
small_discount = .80
medium_discount = .70
large_discount = .50

#Define the intro function.
def intro():
      #Display a welcome message for your program.
      print("Welcome to the Fiber Optic Cable Installation Calculator.\n"
            "This program will calculate the cost of installing fiber optic cable with\n"
            "The Fictitious Fiber Optic Cable Company.\n"
            "\n"
            "The cost per foot of fiber optic cable is as follows:\n"
            f"Less than 100 feet: ${no_discount:.2f} per foot.\n"
            f"100 to 250 feet: ${small_discount:.2f} per foot.\n"
            f"250 to 500 feet: ${medium_discount:.2f} per foot.\n"
            f"More than 500 feet: ${large_discount:.2f} per foot.")

#Define the main function.
def main():

      #Print a blank line for readability.
      print()

      #Get the number of feet of fiber optic to be installed from the user and store it in a variable.
      number_of_feet = float(input("Enter the number of feet of fiber optic cable to be installed: "))

      #Print a blank line for readability.
      print()

      #Use an if-elif-else statement to evaluate the total cost based on the number of feet requested.
      if number_of_feet <= 0:
            print("Invalid input. Please enter a positive number of feet.")
            main()
            return
      elif number_of_feet < 100:
            total_cost = number_of_feet * no_discount
      elif number_of_feet < 250:
            total_cost = number_of_feet * small_discount
      elif number_of_feet < 500:
            total_cost = number_of_feet * medium_discount
      else:
            total_cost = number_of_feet * large_discount

      #Display the calculated information and company name to the user.
      print(f"Your total cost for installing {number_of_feet} feet of fiber optic cable is ${total_cost:,.2f}.\n"
          "\n"
          "Thank you for choosing The Fictitious Fiber Optic Cable Company.\n"
          "for your fiber optic cable installation needs.")


#Call the intro function.
intro()

#Call the main function.
main()
