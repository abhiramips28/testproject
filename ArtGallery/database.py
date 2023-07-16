import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'abhirami')
# print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Art_Gallery")

mycursor.execute("use art_gallery")
#
# mycursor.execute("create table customer(ID int AUTO_INCREMENT not null primary key,NAME varchar(250) not null,"
#                  "MOBILE_NUMBER int not null,GMAIL varchar(250)not null,PASSWORD varchar(250)not null);")
# mycursor.execute("show tables")


