import mysql.connector
# connecting python3 to mysql

# connecting to my sql 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="flute",
  database="todo" # THE DATABASE YOU'RE CREATING THE TABLE FOR 
)

# creating  tables named tasks and users
mycursor = mydb.cursor()

# We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a 
# unique number for each record. Starting at 1, and increased by one for each record.

mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, user_id BIGINT(20), user_login VARCHAR(100), user_password VARCHAR(64), user_firstname VARCHAR(50), user_surname VARCHAR(50), user_email VARCHAR(100))")
mycursor.execute("CREATE TABLE tasks (id INT AUTO_INCREMENT PRIMARY KEY, task_id BIGINT(20), user_id BIGINT(20), task_name VARCHAR(60), task_priority TINYINT(2), task_color VARCHAR(7), task_description VARCHAR(150), task_attendees VARCHAR(4000))")


# # CHeck if Table Exists
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x) 





#  If the table already exists, use the ALTER TABLE keyword:

# mycursor.execute("ALTER TABLE tablename ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute("ALTER TABLE tablename ADD COLUMN country VARCHAR(300)")
