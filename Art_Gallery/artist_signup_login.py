# #
# file=open("artist_login_details.txt",'w')
# file.write("sanjusanjay23@gmail.com-sanju123@""\n"
# "shamendu12@gmail.com-shammu@172""\n"
# "rajrajan12@gmail.com-rajan@142""\n"
# "ganapathi34@gmail.com-ganapathi12@""\n"
# "punekae99@gmail.com-punness21@""\n"
# "sanjusanju@gmail.com-sanju09@""\n"
# "dipti66@gmail.com-dipti88@""\n"
# "ghanshyam44@gmail.com-ghan23@""\n"
# "nayakghana@gmail.com-ghan23@32""\n"
# "rajraj23@gmail.com-rajraj@12""\n"
# "paraspp23@gmail.com-paras@23""\n"
# "sureshsuresh12@gmail.com-susu@01""\n"
# "ganapathi45@gmail.com-ganahana@12""\n"
# "babu123@gmail.com-babu@123""\n")
# file.close()


import mysql.connector


mydb = mysql.connector.connect(host='localhost', user='root', password='abhirami')
# print(mydb)


def signup():
    print("$$$$$$$$$$$$ REGISTER $$$$$$$$$$$$")
    print("\n")
    print("kindly fill in this form to register")
    gmail = input("Enter email address: ")
    mob_no=int(input("Enter mobile number: "))
    user_name=str(input("Enter user name: "))
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if "@gmail.com" in gmail:
        if  type(mob_no)==int and len(str(mob_no))==10:
            if user_name.isalpha()==True or " " in user_name:
                  if conf_pwd == pwd:
                      x=str(gmail)+"-"+str(pwd)
                      with open(r"artist_login_details.txt", 'r+') as fp:
                          for i in fp:
                              if x in i:
                                  print("This account already exists")
                                  signup()
                          else:
                              with open("artist_login_details.txt", "a") as f:
                                   f.write(x)
                              print(" you have successfully registered")
                              print("\n")
                              start()
                  else:
                      print("invalid password")
                      print("\n")
                      signup()
            else:
                print("invalid user name")
                print("user name has only contain alphabets")
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

def login():
    print("$$$$$$$$$$$$ VISUAL FALKS $$$$$$$$$$$$")
    print("\n")
    # print("kindly fill in this form to register")
    gmail = input("Enter gmail: ")
    pwd = input("Enter password: ")
    with open(r"artist_login_details.txt", 'r+') as fp:
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
        print("\n")
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
