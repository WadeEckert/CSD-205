#===================================================================
#Title: Module 4.2 Assignment
#Author: Wade Eckert
#Date: 01 October 2025
#Description: This program demonstrates a simple calculator
#that uses a function to convert miles driven to kilometers.
#The program will then display the total miles and the converted 
#kilometers.
#===================================================================

#Make a variable for the magic number for the conversion rate
CONVERSION_RATE = 1.609244

#Define the main function
def main():
  
    #Prompt the user for the number of miles driven
    #Validate the input to ensure it is a positive number and not a string
    #Use a loop to return the user to the prompt if the input is invalid
    while True:
        try:
            miles = float(input("Enter the number of miles driven: "))
            if miles < 0:
                raise ValueError("The number of miles driven must be a positive number.")
            elif miles == 0:
                raise ValueError("The number of miles driven must be greater than zero.")
            elif miles == "":
                raise ValueError("The number of miles driven must be a positive number.")
            #Exit the loop if input is valid
            break
        except ValueError as e:
            print()
            print("Invalid input. Please enter a positive number.")
            print(e)
            print()
            # The loop continues, prompting the user again

    #Call the miles_to_kilometers function to convert miles to kilometers
    kilometers = miles_to_kilometers(miles)
  
    #Display the total miles and the converted kilometers
    print()
    print("Total miles driven: ", miles)
    print("Total kilometers driven: ", kilometers)

#Define the function to convert miles to kilometers
def miles_to_kilometers(miles):
    #Convert miles to kilometers
    kilometers = miles * CONVERSION_RATE
    #Return the converted kilometers
    return kilometers

#Define the the intro function
def intro():
    print("Miles to Kilometers Converter")
    print("Enter the number of miles driven to convert to kilometers.")
    print()

#Call the intro function
intro()

#Call the main function
main()