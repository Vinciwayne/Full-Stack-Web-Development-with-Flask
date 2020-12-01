import mysql.connector
# connecting python3 to mysql

# connecting to my sql 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="flute"
)

# creating a database named todo
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE todo")


# # Check if Database Exists
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x) 