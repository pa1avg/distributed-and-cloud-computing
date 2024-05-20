import sys
import Pyro5.errors
from Pyro5.api import Proxy

# Check that the Python file rental.py exists.
import os.path
if(os.path.isfile("rental.py")==False):
	print("Error you need to call the Python file rental.py!")

# Check that the class is called rental. That is, the file rental.py contains the expression "rental(object):"
file_text = open('rental.py', 'r').read()
if("rental(object):" not in file_text):
	print("Error you need to call the Python class rental!")

sys.excepthook = Pyro5.errors.excepthook
rental_obj = Proxy("PYRONAME:example.rental")


# Task 1 & 2
# Initialize the remote object rental_obj
rental_obj.add_user("aa", "11")
rental_obj.add_user("bb", "22")
result = rental_obj.return_users()
print()
print("Data returned:")
print(result)
print()
# Task 3 & 4
# Initialize the remote object rental_obj
rental_obj.add_manufacturer("cc", "dd")
rental_obj.add_manufacturer("ee", "ff")
result = rental_obj.return_manufacturers()
print()
print("Data returned:")
print(result)
print()
# Task 5 & 6
# Initialize the remote object rental_obj
result = rental_obj.return_cars_not_rented()
print()
print("Data returned:")
print(result)
print()
rental_obj.add_manufacturer("aa", "dd")
rental_obj.add_manufacturer("bb", "ff")
rental_obj.add_manufacturer("cc", "uu")
rental_obj.add_rental_car("aa", "gg")
rental_obj.add_rental_car("aa", "gg")
rental_obj.add_rental_car("bb", "hh")
result = rental_obj.return_cars_not_rented()
print()
print("Data returned:")
print(result)
print()
# Task 7 & 8
# Initialize the remote object rental_obj
rental_obj.add_user("aa", "11")
rental_obj.add_user("bb", "22")
rental_obj.add_manufacturer("cc", "zz")
rental_obj.add_manufacturer("ee", "xx")
rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")
result = rental_obj.return_cars_rented()
print()
print("Data returned:")
print(result)
print()
result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
print()
print("Data returned:")
print(result)
print()
result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
print()
print("Data returned:")
print(result)
print()
result = rental_obj.return_cars_rented()
print()
print("Data returned:")
print(result)
print()
# Task 9
# Initialize the remote object rental_obj
rental_obj.add_user("aa", "11")
rental_obj.add_user("bb", "22")
rental_obj.add_manufacturer("cc", "zz")
rental_obj.add_manufacturer("ee", "xx")
rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")
result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
result = rental_obj.rent_car("bb", "dd", 2019, 1, 3)
result = rental_obj.return_cars_rented()
print()
print("Data returned:")
print(result)
print()
result = rental_obj.return_cars_not_rented()
print()
print("Data returned:")
print(result)
print()
rental_obj.end_rental("bb", "dd", 2019, 2, 4)
result = rental_obj.return_cars_rented()
print()
print("Data returned:")
print(result)
print()
result = rental_obj.return_cars_not_rented()
print()
print("Data returned:")
print(result)
print()
# Task 10
# Initialize the remote object rental_obj
rental_obj.add_user("aa", "11")
rental_obj.add_user("bb", "22")
rental_obj.add_manufacturer("cc", "zz")
rental_obj.add_manufacturer("ee", "xx")
rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")
result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
rental_obj.delete_car("ff")
rental_obj.delete_car("dd")
result = rental_obj.return_cars_rented()
print()
print("Data returned:")
print(result)
print()
result = rental_obj.return_cars_not_rented()
print()
print("Data returned:")
print(result)
print()
# Task 11
# Initialize the remote object rental_obj
rental_obj.add_user("aa", "11")
rental_obj.add_user("bb", "22")
rental_obj.add_manufacturer("cc", "zz")
rental_obj.add_manufacturer("ee", "xx")
rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")
result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
rental_obj.end_rental("aa", "ff", 2019, 2, 4)
print("The method delete_user should return a value of 1...")
result = rental_obj.delete_user("aa")
print()
print("Data returned:")
print(result)
print()
result = rental_obj.delete_user("bb")
print()
print("Data returned:")
print(result)
print()
result = rental_obj.return_users()
print()
print("Data returned:")
print(result)
print()
# Task 12
# Initialize the remote object rental_obj
rental_obj.add_user("aa", "11")
rental_obj.add_user("bb", "22")
rental_obj.add_manufacturer("cc", "zz")
rental_obj.add_manufacturer("ee", "xx")
rental_obj.add_rental_car("cc", "dd")
rental_obj.add_rental_car("ee", "ff")
result = rental_obj.rent_car("aa", "ff", 2019, 1, 3)
rental_obj.end_rental("aa", "ff", 2019, 2, 4)
result = rental_obj.rent_car("bb", "dd", 2019, 1, 3)
rental_obj.end_rental("bb", "dd", 2019, 2, 4)
result = rental_obj.user_rental_date("aa", 2019, 1, 3, 2019, 3, 4)
print()
print("Data returned:")
print(result)
print()
result = rental_obj.user_rental_date("bb", 2019, 1, 3, 2019, 1, 4)
print()
print("Data returned:")
print(result)
print()


# rental_object.add_user("Conor", "123432")
# rental_object.add_user("Reilly", "67898654")
# rental_object.add_user("Conor Reilly", "12343212")
# print(rental_object.return_users())
# rental_object.add_manufacturer("BMW", "Germany")
# rental_object.add_manufacturer("BMW", "Germany")
# rental_object.add_manufacturer("Audi", "Germany")
# rental_object.add_manufacturer("Benz", "Germany")
# print(rental_object.return_manufacturers())
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("Audi", "Q5")
# rental_object.add_rental_car("Benz", "GLS 300")
# print(rental_object.return_cars_not_rented())
# print(rental_object.rent_car("Conor Reilly", "3 Series", 2024, 1, 1))
# print(rental_object.rent_car("Conor", "Q5", 2024, 1, 10))
# print(rental_object.return_cars_rented())
# print(rental_object.end_rental("Conor Reilly", "3 Series", 2024, 2, 1))
# print(rental_object.return_cars_rented())
# rental_object.delete_car("3 Series")
# print(rental_object.delete_user("Conor Reilly"))
# print(rental_object.user_rental_date("Conor", 2024, 1, 1, 2024, 3, 1))

# rental_object.add_user("Conor Reilly", "12343212")
# print(rental_object.return_users())
#rental_object.add_manufacturer("BMW", "Germany")
# print(rental_object.return_manufacturers())
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("BMW", "3 Series")
print(rental_object.return_cars_not_rented())
# print(rental_object.rent_car("Conor Reilly", "3 Series", 2019, 1, 3))
# print(rental_object.return_cars_rented())
# print(rental_object.end_rental("Conor Reilly", "3 Series", 2019, 2, 4))
# rental_object.delete_car("3 Series")
# print(rental_object.delete_user("Conor Reilly"))
# print(rental_object.user_rental_date("Conor Reilly", 2010, 1, 1, 2029, 2, 1))

# rental_object.add_user("Conor", "123456")
# # rental_object.add_user("Conor Reilly", "123356")
# rental_object.add_user("Anubhav", "123356")
# rental_object.add_user("Deepak", "124356")
# rental_object.add_user("Surabhi", "124256")
# rental_object.add_user("Shraddha", "114356")
# rental_object.add_user("Rohan", "124355")
 
 
# #Task 2
# print(rental_object.return_users())
 
# #Task 3
# rental_object.add_manufacturer("BMW", "Germany")
# rental_object.add_manufacturer("Mercedes", "India")
 
# #Task 4
# print(rental_object.return_manufacturers())
 
# #Task 5
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("BMW", "X5")
# rental_object.add_rental_car("Mercedes", "A8")
# rental_object.add_rental_car("Mercedes", "A9")
# # rental_object.add_rental_car("Mercedes", "A8")
 
 
# #Task 6
# print(rental_object.return_cars_not_rented())
 
# # Task 7
# print(rental_object.rent_car("Conor", "3 Series", 2019, 1, 3))
# print(rental_object.rent_car("Anubhav", "3 Series", 2019, 1, 4))
# print(rental_object.rent_car("Deepak", "3 Series", 2019, 1, 4))
# print(rental_object.rent_car("Surabhi", "X5", 2019, 1, 4))
# print(rental_object.rent_car("Shraddha", "A8", 2019, 1, 4))
# print(rental_object.rent_car("Rohan", "A8", 2019, 1, 4))
# print(rental_object.return_cars_not_rented())
 
 
# #Task 8
# print(rental_object.return_cars_rented())
 
 
# #Task 9
# print(rental_object.end_rental("Conor", "3 Series", 2019, 2, 4))
# print(rental_object.end_rental("Surabhi", "X5", 2019, 2, 4))
# print(rental_object.return_cars_not_rented())
 
# print(rental_object.return_cars_rented())
 
# #Task 10
# rental_object.delete_car("3 Series")
# print(rental_object.return_cars_rented())
# print(rental_object.return_cars_not_rented())
 
# #Task 11
# print(rental_object.delete_user("Anubhav"))
# print(rental_object.delete_user("Conor"))
 
# # # # #Task 12
# print(rental_object.user_rental_date("Conor", 2019, 1, 1, 2029, 2, 1))
# print(rental_object.user_rental_date("Anubhav", 2019, 1, 1, 2029, 2, 1))

###ADD USERS
# rental_object.add_user("Conor Reilly", "12343212")
# rental_object.add_user("Bannu", "23422")
# rental_object.add_user("Pavu", "234543")
# rental_object.add_user("Pavan", "5678876")
# rental_object.add_user("Babe", "1236876")
# ###VIEW USERS
#print(rental_object.return_users())
# ###ADD MANUFACTURER
# rental_object.add_manufacturer("BMW", "Germany")
# rental_object.add_manufacturer("Audi", "Germany")
# rental_object.add_manufacturer("Benz", "Germany")
# ###VIEW MANUFACTURER
# #print(rental_object.return_manufacturers())
# ###ADD CARS
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("BMW", "3 Series")
# rental_object.add_rental_car("Audi", "Q5")
# rental_object.add_rental_car("Benz", "GLS 300")
# rental_object.add_rental_car("BMW", "5 Series")
# rental_object.add_rental_car("Audi", "Q3")
###VIEW AVAILABLE CARS
#print(rental_object.return_cars_not_rented())
###GIVE CAR FOR RENT
#print(rental_object.rent_car("Conor Reilly", "3 Series", 2019, 1, 3))
#print(rental_object.rent_car("Conor Reilly", "3 Series", 2019, 3, 3))
#print(rental_object.rent_car("Bannu", "Q5", 2019, 2, 3))
###VIEW RENTED CARS
#print(rental_object.return_cars_rented())
###END RENT
#print(rental_object.end_rental("Conor Reilly", "3 Series", 2019, 2, 4))
#print(rental_object.end_rental("Conor Reilly", "3 Series", 2019, 4, 4))
###VIEW AVAILABLE CARS
#print(rental_object.return_cars_not_rented())
###Delete Cars 
#rental_object.delete_car("3 Series")
###print(rental_object.return_cars_not_rented())
###Delet User
#print(rental_object.delete_user("Pavan"))

