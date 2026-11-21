import sqlite3

# Create the database
connection = sqlite3.connect('nittanyRide.db')

# Cursur for later use
cursor = connection.cursor()

# Temp drop tables
cursor.execute("DROP TABLE IF EXISTS User")

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

print("User Table: \n")
with open('user.csv', 'r') as userFile:
  for row in userFile:
    cursor.execute("INSERT INTO User (email_address, password, first_name, last_name, phone_number) VALUES (?,?,?,?,?)", row.rstrip("\n").split(","))
    connection.commit()
print("\n")

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