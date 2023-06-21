import mysql.connector

# Create a MySQL connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Anurag12345#",
  auth_plugin='mysql_native_password',
)

# Create the database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Resumes")
print('Database created Successfully!!')

# Create the users table
mycursor.execute("USE Resumes")
mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT(11) NOT NULL AUTO_INCREMENT, name VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL, PRIMARY KEY (id))")
print('Users table created sucessfully!!!')

# Create the resumes table
mycursor.execute("CREATE TABLE IF NOT EXISTS resumes (id INT(11) NOT NULL AUTO_INCREMENT, filename VARCHAR(255) NOT NULL, PRIMARY KEY (id))")
print('Resumes table created sucessfully!!!')

# Close the MySQL connection
mycursor.close()
mydb.close()
