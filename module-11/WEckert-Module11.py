#======================================================================
#Title: Module 11.2 Assignment
#Author: Wade Eckert
#Date: 22 November 2025
#Description: The program takes a number from the user and prints
#the numbers from 1 up to and including that number. The program uses
#two functions to do this. The first function is recursive and the
#second function is non-recursive.
#======================================================================

#Define the recursive function
#The recursive function works by calling itself with n-1 as input until n is 1. 
#Then it prints 1 and returns. The function then prints n and returns. 
#This process continues until n is 0.
def recursive(n):
  #If the input is 1, print 1
  if n == 1:
    print(1, end=" ")
    return
  #If the input is greater than 1, print n and call the function again with n-1 as input
  else:
    recursive(n-1)
    print(n, end=" ")
    return

#Define the non-recursive function
#The non-recursive function works by using a for loop to print 1 up to and including n. 
#The for loop starts at 0 and ends at n-1. The loop prints i+1 for each iteration.
def non_recursive(n):
  for i in range(n):
    print(i+1, end=" ")

#Define the introducton function to the program
def introduction():
  print("This program prints takes a number from the user and prints")
  print("the numbers from 1 up to and including that number.")
  print("The program uses two functions to do this.")
  print("The first function is recursive and the second function is non-recursive.")

#Call the introduction function
introduction()
print()

#Ask the user for an input
while True:
  try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
      print("\nPlease enter a positive integer greater than 0.\n")
    else:
      break
  except ValueError:
    print("\nInvalid input. Please enter an integer.\n")  
print()

#Call the recursive function
print("Recursive function:")
recursive(n)
print("\n")

#Call the non-recursive function
print("Non-recursive function:")
non_recursive(n)