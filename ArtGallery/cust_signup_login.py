import mysql.connector


my_db = mysql.connector.connect(host = 'localhost',user = 'root',password = 'abhirami')
# print(my_db)
#
mycursor = my_db.cursor()

mycursor.execute("use art_gallery")

#query to create a customer table
# query="CREATE TABLE CUSTOMER (name VARCHAR(10),mob_no int,gmail VARCHAR(20),password VARCHAR(50),confirm_password varchar(50))"
# mycursor.execute(query) #executing the query



#query to create a register table
# query1="CREATE TABLE register(custName VARCHAR(20),custAddress VARCHAR(10),pin_code int,phn_no int)"
# mycursor.execute(query1) #executing the query




def signup():
    print("$$$$$$$$$$$$ SIGNUP $$$$$$$$$$$$")
    print("kindly fill in this form to signup")
    name = input("Enter the name: ")
    gmail = input("Enter email address: ")
    mob_no= int(input("Enter mobile number"))
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if name.isalpha()==True or" " in name:
       if "@gmail.com" in gmail:
           if type(mob_no)==int and len(str(mob_no))==10:

                  if conf_pwd == pwd:
                      x=str(gmail)+"-"+str(pwd)
                      with open("customer_details.txt", 'w+') as fp:
                          for i in fp:
                              if x in i:
                                  print("This account already exists")
                                  signup()
                          else:
                              with open("customer_details.txt", "a") as f:
                                   f.write(x)
                              print(" you have successfully registered")
                              print("\n")
                              start()
                  else:
                      print("invalid password")
                      print("\n")
                      signup()

           else:
             print("invalid mobile number")
             print("\n")
             signup()
       else:
        print("invalid gmail")
        print("\n")
        signup()
    else:
        print("invalid name")
        print("\n")
        signup()

def login():
    print("$$$$$$$$$$$$ VISUAL FALKS $$$$$$$$$$$$")
    print("\n")
    # print("kindly fill in this form to register")
    gmail = input("Enter gmail: ")
    pwd = input("Enter password: ")
    with open("customer_details.txt", 'r+') as fp:
        w = str(gmail)+"-"+pwd
        for i in fp:
            if w in i:
                print( "Logged in Successfully!!!!")
                start()
                break
        else:
            print( "An error occurred with log in....")
            login()
def start():

    while 1:
        print("********** Login System **********")

        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        ch = int(input("Enter your choice: "))
        print("\n")
        if ch == 1:
            signup()
        elif ch == 2:
            login()
        elif ch == 3:
            break
        else:
            print("Wrong Choice!")

start()