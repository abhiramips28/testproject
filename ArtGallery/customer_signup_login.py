import mysql.connector

my_db = mysql.connector.connect(host = 'localhost',user = 'root',password = 'abhirami')
# print(my_db)

mycursor = my_db.cursor()

mycursor.execute("use art_gallery")

#query to create a customer table
# query="CREATE TABLE CUSTOMER (name VARCHAR(10),mob_no int,gmail VARCHAR(20),password VARCHAR(50),confirm_password varchar(50))"
# mycursor.execute(query) #executing the query



#query to create a register table
# query1="CREATE TABLE register(custName VARCHAR(20),custAddress VARCHAR(10),pin_code int,phn_no int)"
# mycursor.execute(query1) #executing the query


#query to create a product table
# query2="CREATE TABLE product(date VARCHAR(20),product_name VARCHAR(10),price int)"
# mycursor.execute(query2) #executing the query







def customer():
    l=1
    for l in range(1,3):
        choice = int(input("ENTER THE CHOICE: "))
        if choice == 0:
         from log import customer
         customer()
         f()
        print("CHOOSE: 1-LOGIN , 2-REGISTER ")
        choice = int(input("ENTER THE CHOICE: "))
        if choice == 1:
            c=1
            while c < 3:
                if c == 1:
                    name= str(input("USER NAME:"))
                    password = input("PASSWORD:")
                    break
                elif c == 2:
                    name = str(input("ENTER THE NAME:"))
                    gmailid = input("ENTER THE G-MAIL ID:")
                    mobno = int(input("ENTER THE MOB-NO:"))
                    password = input("ENTER THE PASSWORD:")
                    repassword = input("RE-ENTER THE PASSWORD:")
                    if password != repassword:
                        print("invalid password")
                        break
                    else:
                        print("registration completed ")
                        break

# choice = int(input("ENTER THE CHOICE:"))
customer()























