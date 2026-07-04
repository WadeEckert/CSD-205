#===================================================================
#Title: Module 6.2 Assignment
#Author: Wade Eckert
#Date: 13 October 2025
#Description: This program demonstrates a program that creates a 
#tuple, iterates through the tuple, and displays the output as
#a single sentence using each value. The program then reverses the 
#output and displays it as a single sentence with a different
#context string.
#===================================================================

#Define the main function.
def main():
  #Create a Tuple initialized with 15 to 25 related values.
  cars = ("Ford", "Chevy", "Toyota", "Honda", "Dodge", "Jeep", "BMW", "Mercedes", "Audi", "Volkswagen", "Tesla", "Nissan", "Mazda", "Subaru", "Hyundai", "Kia", "Volvo", "Lexus", "Acura", "Mitsubishi")
  #Display the contents in a single statement.
  print(f"The contents of the tuple are: \n"
        f"{cars}")
  print()
  #Call the function to display the contents of the tuple and print the sentence.
  sentence = display_cars(cars)
  print(sentence)
  print()
  #Call the function to display the contents of the tuple in reverse order and print the sentence.
  reverse_sentence = reverse_display(cars[::-1])
  print(reverse_sentence)
  
#Define a function for displaying the contents of the tuple.
def display_cars(cars):
  #Initialize a sentence string.
  sentence = "I wish I had a "
  #Iterate through the tuple and add each value to the sentence string.
  for i, car in enumerate(cars):
    if i < len(cars) - 2:
      sentence += f"{car}, "
    elif i == len(cars) - 2:
      sentence += f"{car}, and a "
    else:
      sentence += f"{car} in my garage."
  return sentence

#Define a function to display the contents of a tuple in reverse order.
def reverse_display(cars):
  #Initialize a sentence string.
  sentence = "My favorite car brands in order are: "
  #Iterate through the tuple and add each value to the sentence string.
  for i, car in enumerate(cars):
    if i < len(cars) - 2:
      sentence += f"{car}, "
    elif i == len(cars) - 2:
      sentence += f"{car}, and "
    else:
      sentence += f"{car}."
  return sentence

#Define the intro function.
def intro():
  print("This program demonstrates tuple creation and iteration.")
  print("It displays the tuple's contents in a single sentence.")
  print("Then, it reverses the tuple and displays it with a different sentence.")
  print()

#Call the intro function.
intro()
  
#Call the main function.
if __name__ == "__main__":
   main()