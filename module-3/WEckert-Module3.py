#===================================================================
#Title: Module 3.2 Assignment
#Author: Wade Eckert
#Date: 21 September 2025
#Description: This program demonstrates the use of a while loop to 
#determine how long it takes for an investment to double at a given 
#interest rate.
#The interest is calculated using the formula: 
#interest amount = (principal investment * rate * 1)/100
#===================================================================

#Define the intro function.
def intro():
  print("This program will calculate how many years it will take an initial investment\n"
        "to double at a given annualized interest rate.")
  print()
  
#Define the main function.
def main():

  #Get the initial investment amount.
  initial_investment = float(input("Enter the initial investment amount: "))

  #Print a blank line for clarity.
  print()

  #Get the annualized interest rate.
  interest_rate =  float(input("Enter the annualized interest rate for the initial investment amount: "))

  #Print a blank line for clarity.
  print()

  #Calculate the number of years it takes for the investment to double.
  
  #Initialize the number of years.
  years = 0
  
  #Initialize the current investment amount.
  current_investment = initial_investment

  #Use a while loop to calculate the number of years it takes for the investment to double.
  while current_investment < initial_investment * 2:
    #Calculate the interest amount for the current year.
    interest_amount = (current_investment * interest_rate * 1)/100
    #Add the interest amount to the current investment amount.
    current_investment = current_investment + interest_amount
    #Increment the number of years.
    years += 1

  #Display the number of years it takes for the investment to double.
  print("It will take", years, "years for the investment to double.")

#Call the intro function.
intro()

#Call the main function.
main()
