#===================================================================
#Title: Module 1.3 Assignment
#Author: Wade Eckert
#Date: 09 September 2025
#Description: This program demonstrates a simple calculator 
#for calculating the cost of installing fiber optic cable for 
#a fictitious company. This program demonstrates the print, input, and float
#functions and variable assignment statements.
#===================================================================

#Make a named constant variable for the magic number .87
cost_per_foot = .87

#Display a welcome message for your program.
print("Welcome to the Fiber Optic Cable Installation Calculator.\n"
      "This program will calculate the cost of installing fiber optic cable with\n"
      "The Fictitious Fiber Optic Cable Company.")

#Print a blank line for readability.
print()  

#Get the number of feet of fiber optic to be installed from the user and store it in a variable.
number_of_feet = float(input("Enter the number of feet of fiber optic cable to be installed: "))

#Print a blank line for readability.
print()

#Calculate the total cost as the number of feet the user supplied times .87 and store it in a variable.
total_cost = number_of_feet * cost_per_foot

#Display the calculated information and company name to the user.
print(f"Your total cost for installing {number_of_feet} feet of fiber optic cable is ${total_cost:,.2f}.")
print()
print("Thank you for choosing The Fictitious Fiber Optic Cable Company "
      "for your fiber optic cable installation needs.")