from argon2 import PasswordHasher
import sqlite3

ph = PasswordHasher()
connection = sqlite3.connect("nittanyRide.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

rows = cursor.execute("SELECT email_address, password FROM User").fetchall()

for (email,password) in rows:
  if password.startswith("$argon2"):
    continue
  new_hash = ph.hash(password)
  cursor.execute("UPDATE User SET password = ? WHERE email_address = ?", (new_hash, email))

connection.commit()
connection.close()