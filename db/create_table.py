import mysql.connector;

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password = "password"
)

db_name = "gmail_api_demo"
table_name = "gmail_msgs"

cursor = mydb.cursor()
cursor.execute("create database if not exists "+ db_name)
cursor.execute("use "+ db_name)

cursor.execute("create table if not exists " + table_name + 
               "(id int primary key auto_increment, msg_id varchar(50) unique not null, thread_id varchar(50) not null, date_received timestamp not null, internal_date timestamp not null, subject varchar(200) not null, from_address varchar(200) not null, body text, created_at timestamp)")

print("======== Successfully created database and tables ========")




