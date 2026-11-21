import sqlite3

# Create the database
connection = sqlite3.connect('nittanyride.db')

# Cursur for later use
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS User")
cursor.execute("DROP TABLE IF EXISTS Rider")
cursor.execute("DROP TABLE IF EXISTS Driver")
cursor.execute("DROP TABLE IF EXISTS Support_Staff")
cursor.execute("DROP TABLE IF EXISTS Home_Address")
cursor.execute("DROP TABLE IF EXISTS Payment_Information")
cursor.execute("DROP TABLE IF EXISTS Vehicle_Information")
cursor.execute("DROP TABLE IF EXISTS Ride_Type_Application")


# Need to enable foreign key support in sqlite
cursor.execute("PRAGMA foreign_keys = ON;")

# Create the tables for the database
# User table
user_table = """
CREATE TABLE if not exists User (
  email_address TEXT Primary Key NOT NULL CHECK (length(email_address) <=30 ), 
  password TEXT NOT NULL CHECK (length(password) <= 250), 
  first_name TEXT CHECK (length(first_name) <= 25), 
  last_name TEXT CHECK (length(last_name) <= 25), 
  phone_number TEXT
)
"""
try:
  cursor.execute(user_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()

print("User Table: ")
with open('csv_files/user.csv', 'r') as userFile:
  for row in userFile:
    cursor.execute("INSERT INTO User (email_address, password, first_name, last_name, phone_number) VALUES (?,?,?,?,?)", row.rstrip("\n").split(","))
    connection.commit()
print("")

userExec = cursor.execute("SELECT * FROM User").fetchall()
for i in userExec:
  print(i)

# Rider table
rider_table = """
CREATE TABLE if not exists Rider (
  rider_email_address TEXT Primary Key NOT NULL CHECK (length(rider_email_address) <=30 ), 
  rider_type TEXT CHECK (length(rider_type) <= 15),
  Foreign Key (rider_email_address) References User (email_address)
)
"""
try:
  cursor.execute(rider_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()

print("\nRider Table: ")
with open('csv_files/rider.csv', 'r') as riderFile:
  for row in riderFile:
    cursor.execute("INSERT INTO Rider (rider_email_address, rider_type) VALUES (?,?)", row.rstrip("\n").split(","))
    connection.commit()
print("")

riderExec = cursor.execute("SELECT * FROM Rider").fetchall()
for i in riderExec:
  print(i)


# Driver table
driver_table = """
CREATE TABLE if not exists Driver (
  driver_email_address TEXT Primary Key NOT NULL CHECK (length(driver_email_address) <=30 ),  
  availability TEXT CHECK (length(availability) <= 15), 
  rating Decimal(2, 1),
  Foreign Key (driver_email_address) References User (email_address)
)
"""
try:
  cursor.execute(driver_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()

print("\nDriver Table: ")
with open('csv_files/driver.csv', 'r') as driverFile:
  for row in driverFile:
    cursor.execute("INSERT INTO Driver (driver_email_address, availability, rating) VALUES (?,?,?)", row.rstrip("\n").split(","))
    connection.commit()
print("")

driverExec = cursor.execute("SELECT * FROM Driver").fetchall()
for i in driverExec:
  print(i)


# Support Staff table
support_staff_table = """
CREATE TABLE if not exists Support_Staff (
  support_email_address TEXT Primary Key NOT NULL CHECK (length(support_email_address) <=30 ), 
  position TEXT CHECK (length(position) <= 15),
  Foreign Key (support_email_address) References User (email_address)
)
"""
try:
  cursor.execute(support_staff_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()

print("\nSupport Staff Table: ")
with open('csv_files/support_staff.csv', 'r') as supportFile:
  for row in supportFile:
    cursor.execute("INSERT INTO Support_Staff (support_email_address, position) VALUES (?,?)", row.rstrip("\n").split(","))
    connection.commit()
print("")

supportExec = cursor.execute("SELECT * FROM Support_Staff").fetchall()
for i in supportExec:
  print(i)


# Home Address table
home_address_table = """
CREATE TABLE if not exists Home_Address (
  account_email_address TEXT Primary Key NOT NULL CHECK (length(account_email_address) <=30 ),
  street TEXT CHECK (length(street) <= 30), 
  city TEXT CHECK (length(city) <= 30), 
  state TEXT CHECK (length(state) <= 30), 
  zip_code TEXT CHECK (length(zip_code) <= 5),
  Foreign Key (account_email_address) References User (email_address)
)
"""
try:
  cursor.execute(home_address_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()

print("\nHome Address Table: ")
with open('csv_files/home_address.csv', 'r') as addrsFile:
  for row in addrsFile:
    cursor.execute("INSERT INTO Home_Address (account_email_address, street, city, state, zip_code) VALUES (?,?,?,?,?)", row.rstrip("\n").split(","))
    connection.commit()
print("")

addrsExec = cursor.execute("SELECT * FROM Home_Address").fetchall()
for i in addrsExec:
  print(i)


# Payment Information table
payment_information_table = """
CREATE TABLE if not exists Payment_Information (
  card_ID TEXT Primary Key NOT NULL CHECK (length(card_id) <= 30), 
  rider_email_address TEXT NOT NULL CHECK (length(rider_email_address) <= 30),  
  card_type TEXT NOT NULL CHECK (length(card_type) <= 25), 
  card_number TEXT NOT NULL CHECK (length(card_number) <= 16), 
  expiration_date DATETIME NOT NULL, 
  security_code TEXT NOT NULL CHECK (length(security_code) <= 3),
  Foreign Key (rider_email_address) References Rider (rider_email_address)
)
"""
try:
  cursor.execute(payment_information_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()

print("\nPayment Information Table: ")
with open('csv_files/payment_information.csv', 'r') as payFile:
  for row in payFile:
    cursor.execute("INSERT INTO Payment_Information (card_ID, rider_email_address, card_type, card_number, expiration_date, security_code) VALUES (?,?,?,?,?,?)", row.rstrip("\n").split(","))
    connection.commit()
print("")

payExec = cursor.execute("SELECT * FROM Payment_Information").fetchall()
for i in payExec:
  print(i)


# Vehicle Information table
vehicle_information_table = """
CREATE TABLE if not exists Vehicle_Information (
  vehicle_ID TEXT Primary Key NOT NULL CHECK (length(vehicle_id) <= 9), 
  driver_email_address TEXT NOT NULL CHECK (length(driver_email_address) <= 30), 
  make TEXT CHECK (length(make) <= 25), 
  model TEXT CHECK (length(model) <= 25), 
  color TEXT CHECK (length(color) <= 25), 
  year TEXT CHECK (length(year) <= 4),
  license_plate_number TEXT NOT NULL CHECK (length(license_plate_number) <= 9),
  Foreign Key (driver_email_address) References Driver (driver_email_address)
)
"""
try:
  cursor.execute(vehicle_information_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()

print("\nVehicle Information Table: ")
with open('csv_files/vehicle_information.csv', 'r') as vFile:
  for row in vFile:
    cursor.execute("INSERT INTO Vehicle_Information (vehicle_ID, driver_email_address, make, model, color, year, license_plate_number) VALUES (?,?,?,?,?,?,?)", row.rstrip("\n").split(","))
    connection.commit()
print("")

vExec = cursor.execute("SELECT * FROM Vehicle_Information").fetchall()
for i in vExec:
  print(i)


# Ride Type Application table
ride_type_application_table = """
CREATE TABLE if not exists Ride_Type_Application (
  application_ID TEXT Primary Key NOT NULL CHECK (length(application_ID) <=9), 
  driver_email_address TEXT NOT NULL CHECK (length(driver_email_address) <= 30),
  support_email_address TEXT NOT NULL CHECK (length(support_email_address) <= 30),  
  date DATETIME NOT NULL, 
  category TEXT CHECK (length(category) <= 25), 
  fare_rate Decimal(5, 2), 
  reason TEXT CHECK (length(reason) <= 250), 
  description TEXT CHECK (length(description) <= 250), 
  application_status TEXT CHECK (length(application_status) <= 25),
  Foreign Key (driver_email_address) References Driver (driver_email_address),
  Foreign Key (support_email_address) References Support_Staff (support_email_address)
)
"""
try:
  cursor.execute(ride_type_application_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()

print("\nRide Type Application Table: ")
with open('csv_files/ride_type_application.csv', 'r') as rideappFile:
  for row in rideappFile:
    cursor.execute("INSERT INTO Ride_Type_Application (application_ID, driver_email_address, support_email_address, date, category, fare_rate, reason, description, application_status) VALUES (?,?,?,?,?,?,?,?,?)", row.rstrip("\n").split(","))
    connection.commit()
print("")

rideappExec = cursor.execute("SELECT * FROM Ride_Type_Application").fetchall()
for i in rideappExec:
  print(i)


# Categories table
categories_table = """
CREATE TABLE if not exists Categories (
  category_ID TEXT Primary Key NOT NULL CHECK (length(category_ID) <= 9),
  category_name TEXT NOT NULL CHECK (length(category_name) <= 30)
)
"""
try:
  cursor.execute(categories_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()


# Ride Offering table
ride_offering_table = """
CREATE TABLE if not exists Ride_Offerings (
  ride_offering_ID TEXT Primary Key NOT NULL CHECK (length(ride_offering_ID) <= 9), 
  driver_email_address TEXT NOT NULL CHECK (length(driver_email_address) <= 30),
  vehicle_ID TEXT NOT NULL CHECK (length(vehicle_ID) <= 9), 
  category_ID TEXT NOT NULL CHECK (length(category_ID) <= 9), 
  description TEXT CHECK (length(description) <= 250), 
  availability TEXT CHECK (length(availability) <= 25), 
  fare_rate Decimal(3, 2) NOT NULL, 
  seat_capacity INTEGER,
  Foreign Key (driver_email_address) References Driver (driver_email_address),
  Foreign Key (vehicle_ID) References Vehicle_Information (vehicle_ID),
  Foreign Key (category_ID) References Categories (category_ID)
)
"""
try:
  cursor.execute(ride_offering_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()


# Ride Request table
ride_request_table = """
CREATE TABLE if not exists Ride_Requests (
  ride_request_ID TEXT Primary Key NOT NULL CHECK (length(ride_request_ID) <= 9), 
  rider_email_address TEXT NOT NULL CHECK (length(rider_email_address) <= 30),
  ride_offering_ID TEXT NOT NULL CHECK (length(ride_offering_ID) <= 9),
  date DATETIME NOT NULL,
  number_seats INTEGER NOT NULL,
  status TEXT NOT NULL CHECK (length(status) <= 15),
  total_price DECIMAL (3, 2),
  Foreign Key (rider_email_address) References Rider (rider_email_address),
  Foreign Key (ride_offering_ID) References Ride_Offerings (ride_offering_ID)
)
"""
try:
  cursor.execute(ride_request_table)
except Exception as e:
  print(e)
  connection.rollback()
  connection.close()