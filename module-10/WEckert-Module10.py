#======================================================================
#Title: Module 10.2 Assignment
#Author: Wade Eckert
#Date: 15 November 2025
#Description: This program demonstrates the use of classes and inheritance.
#It creates two classes, Employee and ProductionWorker, and uses them to create
#two instances of each class. It then displays the information for each instance.
#It also demonstrates the use of getter and setter methods.
#======================================================================

#Define the Employee class that has four fields: the employee name, employee gender, 
#employee hourly pay rate, and the employee number.
class Employee:
  def __init__(self, name, gender, hourly_pay_rate, employee_number):
    self.__name = name
    self.__gender = gender
    self.__hourly_pay_rate = hourly_pay_rate
    self.__employee_number = employee_number

  #Define the getter methods for the Employee class
  def get_name(self):
    return self.__name
  def get_gender(self):
    return self.__gender
  def get_hourly_pay_rate(self):
    return self.__hourly_pay_rate
  def get_employee_number(self):
    return self.__employee_number

  #Define the setter methods for the Employee class
  def set_name(self, name):
    self.__name = name
    return self.__name
  def set_gender(self, gender):
    self.__gender = gender
    return self.__gender
  def set_hourly_pay_rate(self, hourly_pay_rate):
    self.__hourly_pay_rate = hourly_pay_rate
    return self.__hourly_pay_rate
  def set_employee_number(self, employee_number):
    self.__employee_number = employee_number
    return self.__employee_number


#Define the ProductionWorker class that inherits from the Employee class 
#and has one field: the shift number.
class ProductionWorker(Employee):

  def __init__(self, name, gender, hourly_pay_rate, employee_number, shift_number):
    super().__init__(name, gender, hourly_pay_rate, employee_number)
    self.__shift_number = shift_number

  #Define the getter methods for the ProductionWorker class
  def get_shift_number(self):
    return self.__shift_number

  #Define the setter methods for the ProductionWorker class
  def set_shift_number(self, shift_number):
    self.__shift_number = shift_number
    return self.__shift_number


#Define the Main class that uses the Employee and ProductionWorker classes.
class Main:
  def __init__(self):
    #Create two instances of the Employee class
    self.employee1 = Employee("John Doe", "Male", 20.00, 12345)
    self.employee2 = Employee("Jane Smith", "Female", 25.00, 67890)

    #Create two instances of the ProductionWorker class
    self.production_worker1 = ProductionWorker("Bob Johnson", "Male", 22.00, 11223, 1)
    self.production_worker2 = ProductionWorker("Sally Jones", "Female", 23.00, 44556, 2)

    #Set the values for the Employee class instances
    self.employee1.set_name("John Doe")
    self.employee1.set_gender("Male")
    self.employee1.set_hourly_pay_rate(20.00)
    self.employee1.set_employee_number(12345)

    self.employee2.set_name("Jane Smith")
    self.employee2.set_gender("Female")
    self.employee2.set_hourly_pay_rate(25.00)
    self.employee2.set_employee_number(67890)

    #Set the values for the ProductionWorker class instances
    self.production_worker1.set_name("Bob Johnson")
    self.production_worker1.set_gender("Male")
    self.production_worker1.set_hourly_pay_rate(22.00)
    self.production_worker1.set_employee_number(11223)
    self.production_worker1.set_shift_number(1)

    self.production_worker2.set_name("Sally Jones")
    self.production_worker2.set_gender("Female")
    self.production_worker2.set_hourly_pay_rate(23.00)
    self.production_worker2.set_employee_number(44556)
    self.production_worker2.set_shift_number(2)

    #Display the information for the Employee class instances
    print("Employee 1:")
    print("Name: ", self.employee1.get_name())
    print("Gender: ", self.employee1.get_gender())
    print("Hourly Pay Rate: ", self.employee1.get_hourly_pay_rate())
    print("Employee Number: ", self.employee1.get_employee_number())
    print()
    print("Employee 2:")
    print("Name: ", self.employee2.get_name())
    print("Gender: ", self.employee2.get_gender())
    print("Hourly Pay Rate: ", self.employee2.get_hourly_pay_rate())
    print("Employee Number: ", self.employee2.get_employee_number())
    print()
    print("Production Worker 1:")
    print("Name: ", self.production_worker1.get_name())
    print("Gender: ", self.production_worker1.get_gender())
    print("Hourly Pay Rate: ", self.production_worker1.get_hourly_pay_rate())
    print("Employee Number: ", self.production_worker1.get_employee_number())
    print("Shift Number: ", self.production_worker1.get_shift_number())
    print()
    print("Production Worker 2:")
    print("Name: ", self.production_worker2.get_name())
    print("Gender: ", self.production_worker2.get_gender())
    print("Hourly Pay Rate: ", self.production_worker2.get_hourly_pay_rate())
    print("Employee Number: ", self.production_worker2.get_employee_number())
    print("Shift Number: ", self.production_worker2.get_shift_number())

#Create an instance of the Main class
main = Main()
