#===================================================================
#Title: Module 5.2 Assignment
#Author: Wade Eckert
#Date: 10 October 2025
#Description: This program demonstrates a program that writes to a 
#file and read from a file. The program will prompt the user for
#their name, street address, and phone number.  The program will
#then write the data to a file and read the file and display the
#contents.
#===================================================================

#Define the main function
def main():
  
  #Initialize variables
  file_name = ""
  name = ""
  street_address = ""
  phone_number = ""
  
  #Prompt the user for the file name. Validate the file name. If the file name is not valid, prompt the user again.
  while file_name == "":
    file_name = input("Enter the file name: ")
    print()
    if file_name == "":
      print("Invalid file name. Please try again.")
      print()
    else:
      break
         
  #Prompt the user for their name. Validate the name. If the name is not valid, prompt the user again.
  while name == "":
    name = input("Enter your name: ")
    print()
    if name == "":
      print("Invalid name. Please try again.")
      print()
    else:
      break

  #Prompt the user for their street address. Validate the street address. If the street address is not valid, prompt the user again.
  while street_address == "":
    street_address = input("Enter your street address: ")
    print()
    if street_address == "":
      print("Invalid street address. Please try again.")
      print()
    else:
      break

  #Prompt the user for their phone number. Validate the phone number. If the phone number is not valid, prompt the user again.
  while phone_number == "":
    phone_number = input("Enter your phone number: ")
    print()
    if phone_number == "":
      print("Invalid phone number. Please try again.")
      print()
    else:
      break

  #Call the write_to_file function
  write_to_file(file_name, name, street_address, phone_number)

  #Call the read_from_file function
  read_from_file(file_name)

  #Call the save_data function
  save_data(file_name, name, street_address, phone_number)

#Define the write_to_file function
def write_to_file(file_name, name, street_address, phone_number):
   #Open the file in write mode.
   with open(file_name, "w") as file:
   #Write the username, street address, and phone number to a comma-separated line in the file that your user typed in Step 1.
    file.write(name + "," + street_address + "," + phone_number)
    file.close()
    print("Data written to file.")
    print()
    return

#Define the read_from_file function
def read_from_file(file_name):
   #Open the file in read mode.
   with open(file_name, "r") as file:
      #Read the file and display the contents.
      print("Data read from file:")
      print(file.read())
      file.close()
      return

#Define the save_data function
def save_data(file_name, name, street_address, phone_number):
   #Save the data file as <user input name> data.txt
   with open(name + "data.txt", "w") as file:
      file.write(name + "," + street_address + "," + phone_number)
      file.close()
      print()
      print(f'Data saved to "{name} data.txt" file.')
      print()
      return

#Define the intro function
def intro():
    print("This program demonstrates a program that writes to a file and read from a file.\n"
          "The program will prompt the user for their name, street address, and phone number.\n"
          "The program will then write the data to a file and read the file and display the contents.")
    print()

#Call the intro function
intro()

#Call the main function
main()