import sqlite3

connection = sqlite3.connect("nittanyRide.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

# for row in cursor.execute("SELECT email_address FROM user"):
#   print(row)

cursor.execute("INSERT OR IGNORE INTO Rider (rider_email_address, rider_type) VALUES (?, ?)",('abigail.jones60@example.com', "standard"),)
cursor.execute("INSERT OR IGNORE INTO Driver (driver_email_address, availability, rating) VALUES (?, ?, ?)",('amelia.johnson85@example.com', "full time",7.0),)
cursor.execute("INSERT OR IGNORE INTO Support_Staff (support_email_address, position) VALUES (?, ?)",('ava.white69@mail.com',"technician"),)

connection.commit()

for table in ("Rider", "Driver", "Support_Staff"):
    print(table, cursor.execute(f"SELECT * FROM {table}").fetchall())

connection.close()