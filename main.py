import sqlite3
import pandas as pd

# Create the database
connection = sqlite3.connect('nittanyride.db')

# Create the tables for the database
user_table = """
CREATE TABLE if not exists User (
  email_address varchar(30) Primary Key NOT NULL, 
  password varchar(20) NOT NULL, 
  first_name varchar(25), 
  last_name varchar (25), 
  phone_number char(13)
)
"""

home_address_table = """
CREATE TABLE if not exists Home_Address (
  account_email_address varchar(30) Primary Key,
  street varchar(30), 
  city varchar(30), 
  state varchar(20), 
  zip_code char(5),
  Foreign Key (account_email_address) References User (email_address)
)
"""

rider_table = """
CREATE TABLE if not exists Rider (
  rider_email_address char(30) Primary Key, 
  rider_type varchar(15),
  Foreign Key (rider_email_address) References User (email_address)
)
"""

driver_table = """
CREATE TABLE if not exists Driver (
  driver_email_address varchar(30) Primary Key,  
  availability varchar(15), 
  rating Decimal(1, 1),
  Foreign Key (driver_email_address) References User (email_address)
)
"""

payment_information_table = """
CREATE TABLE if not exists Payment_Information (
  card_ID char (9) Primary Key NOT NULL, 
  rider_email_address varchar(30), 
  card_type varchar(25) NOT NULL, 
  card_number varchar(16) NOT NULL, 
  expiration_date DATETIME NOT NULL, 
  security_code varchar(3) NOT NULL,
  Foreign Key (rider_email_address) References Rider (rider_email_address)
)
"""

vehicle_information_table = """
CREATE TABLE if not exists Vehicle_Information (
  vehicle_ID varchar(9) Primary Key, 
  driver_email_address varchar(30), 
  make varchar(25), 
  model varchar(25), 
  color varchar(25), 
  year varchar(4),
  license_plate_number varchar(8),
  Foreign Key (driver_email_address) References Driver (driver_email_address)
)
"""

ride_request_table = """
CREATE TABLE if not exists Ride_Request (
  request_ID char(9) Primary Key,
  rider_email_address varchar(30),
  Date DATE,
  Status varchar(25),
  Total_price Decimal (3, 2),
  Number_of_seats INTEGER,
  Foreign Key (rider_email_address) References rider (rider_email_address)
)
"""

reviews_table = """
CREATE TABLE if not exists Reviews (
  review_ID char(9) Primary Key, 
  review varchar(250),
  date DATE,
  Rating INTEGER
)
"""

categories_table = """
CREATE TABLE if not exists Categories (
  category_ID char(9) Primary Key,
  category_name varchar(30)
)
"""

ride_offering_table = """
CREATE TABLE if not exists Ride_Offering (
  ride_ID char(9) Primary Key, 
  driver_email_address varchar(30),
  ride_request_ID char(9),
  description varchar(250), 
  availability varchar(25), 
  vehicle_ID varchar(9), 
  fare_rate Decimal(3, 2), 
  category_ID char(9), 
  seat_capacity INTEGER,
  Foreign Key (rider_request_ID) References Ride_Request (rider_request_ID),
  Foreign Key (driver_email_address) References Driver (driver_email_address),
  Foreign Key (vehicle_ID) References Vehicle_Information (vehicle_ID),
  Foreign Key (category_ID) References Categories (category_ID)
)
"""

ride_type_application_table = """
CREATE TABLE if not exists Ride_Type_Application (
  application_ID char(9) Primary Key, 
  driver_email_address varchar(30), 
  date DATETIME, 
  category varchar(25), 
  fare_rate Decimal(3, 2), 
  reason varchar(250), 
  description varchar(250), 
  application_status varchar(25),
  Foreign Key (driver_email_address) References Driver (driver_email_address)
)
"""

support_staff_table = """
CREATE TABLE if not exists Support_Staff (
  PSU_email_address varchar(30) Primary Key, 
  password varchar(20), 
  first_name varchar(25), 
  last_name varchar(25), 
  position varchar(20)
)
"""

cancellation_request_table = """
CREATE TABLE if not exists Cancellation_Request (
  cancellation_ID char(9) Primary Key, 
  ride_offering_ID char(9), 
  status varchar(15), 
  date DATETIME,
  Foreign Key (ride_offering_ID) References Ride_Offering (ride_ID)
)
"""

lost_item_report_table = """
CREATE TABLE if not exists Lost_Item_Report (
  report_ID char(9) Primary Key, 
  rideRequest_ID char(9),
  user_ID  char(30), 
  report_type varchar(15), 
  item_name varchar(25), 
  description varchar(250), 
  imagePath varchar(50),
  date_reported DATETIME, 
  report_status varchar(15), 
  date_resolved DATETIME,
  Foreign Key (rideRequest_ID) References Ride_Offering (ride_ID)
)
"""

questions_table = """
CREATE TABLE if not exists Questions (
  question_ID char(9) Primary Key, 
  question varchar(250), 
  rider_email_address varchar(30), 
  ride_offering_ID char(9),
  Foreign Key (rider_email_address) References Rider (rider_email_address),
  Foreign Key (ride_offering_ID) References Ride_Offering (ride_ID)
)
"""

request_cancellation_table = """
CREATE TABLE if not exists Requests_Cancellation (
  ride_offering_ID char(9), 
  cancellation_request_ID char(9), 
  Primary Key (ride_offering_ID, cancellation_request_ID),
  Foreign Key (ride_offering_ID) References Ride_Offering (ride_ID),
  Foreign Key (cancellation_request_ID) References Cancellation_Request (cancellation_ID)
)
"""

approves_cancellation_table = """
CREATE TABLE if not exists Approves_Cancellation (
  support_email_address varchar(30), 
  cancellation_Request_ID char(9),
  Primary Key (support_email_address, cancellation_request_ID),
  Foreign Key (support_email_address) References Support_Staff (PSU_email_address),
  Foreign Key (cancellation_request_ID) References Cancellation_Request (cancellation_ID)
)
"""

# Execute create table statements
cursor = connection.cursor()
try:
  cursor.execute(user_table)
  cursor.execute(home_address_table)
  cursor.execute(rider_table)
  cursor.execute(driver_table)
  cursor.execute(payment_information_table)
  cursor.execute(vehicle_information_table)
  cursor.execute(ride_request_table)
  cursor.execute(categories_table)
  cursor.execute(reviews_table)
  cursor.execute(ride_offering_table)
  cursor.execute(ride_type_application_table)
  cursor.execute(support_staff_table)
  cursor.execute(cancellation_request_table)
  cursor.execute(lost_item_report_table)
  cursor.execute(questions_table)
  cursor.execute(request_cancellation_table)
  cursor.execute(approves_cancellation_table)
  connection.commit()
except Exception as e:
  print(e)
  connection.rollback()


