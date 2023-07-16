# """write login data in file"""
# file=open("customer_details.txt",'w')
# file.write("janaki001@gmail.com janaki25""\n"
# "manoj2@gmail.com manojk5""\n"
# "varma201@gmail.com varma0010""\n"
# "muhammed8@gmail.com muhammed66""\n"
# "lekha75@gmail.com lekha1002""\n"
# "meghana5@gmail.com meg5hana""\n"
# "jerinj01@gmail.com jerinm202""\n")
# file.close()
# #


import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='abhirami')
mycursor=mydb.cursor()
# print(mydb)

mycursor.execute("use art_gallery")

def signup():
    print("$$$$$$$$$$$$ REGISTER $$$$$$$$$$$$")
    print("\n")
    print("kindly fill in this form to register")
    cust_name = input("NAME : ")
    mob_num = input("MOBILE NUMBER :")
    gmail = input("GMAIL : ")
    pwd = input("PASSWORD : ")
    conf_pwd = input("CONFIRM PASSWORD : ")
    if "@gmail.com" in gmail:
        if conf_pwd == pwd:
            with open(r"customer_details.txt", 'r+') as fp:
                for i in fp:
                    w = i.split()
                    # print(x)
                    if gmail in w or pwd in w:
                        print("This account already exists")
                        break

                else:
                    with open("customer_details.txt", "a") as f:
                        f.write(gmail)
                        f.write(" ")
                        f.write(pwd)
                        f.write("\n")
                    mycursor.execute("use art_gallery")
                    sql = "insert into customer(name,mob_no,gmail,password,confirm_password) values(%s,%s,%s,%s,%s)"
                    val = [
                        (cust_name,mob_num,gmail,pwd),
                    ]
                    mycursor.executemany(sql, val)
                    mydb.commit()
                    print("you have successfully registered")
                    print("\n")
                    start()
        else:
            print("invalid password")
            signup()

    else:
        print("invalid gmail")
        signup()


def login():
    print("$$$$$$$$$$$$ VISUAL FALKS $$$$$$$$$$$$")
    print("\n")
    gmail = input("Enter gmail: ")
    pwd = input("Enter password: ")
    with open(r"customer_details.txt", 'r+') as fp:
        for i in fp:
            x = i.split()
            # print(x)
            if gmail in x and pwd in x:
                # print("Logged in Successfully!!!!")
                print("\n")
                mycursor.execute("use art_gallery")
                mycursor.execute("select*from customer")
                myresult = mycursor.fetchall()
                # print(myresult)
                d = {1:"ID",2:"CUST_NAME",3:"GMAIL",4:"PASSWORD",5:"MOBILE_NUMBER"}
                # print(l)
                dict = {}
                t = 0
                for i in myresult:
                    for x in i:
                        # print(x)
                        t = t + 1
                        dict.setdefault(d.get(t), x)
                    # print(dict)
                    if gmail==dict.get("GMAIL") and pwd==dict.get("PASSWORD"):
                              print("-----------------------------------------------------")
                              print(dict.get("cust_name"))
                              print(dict.get("GMAIL"))
                              print(dict.get("MOBILE_NUMBER"))
                              print("-----------------------------------------------------")

                    dict = {}
                    t = 0
                break
        else:
            print("An error occurred with log in....")
            login()
    print("\n")
    x = input("press * button to go home page")
    start()
def start():
    while 1:
        print("********** Login System **********")
        print("1.Signup")
        print("2.Login")
        print("3.Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            signup()
        elif ch == 2:
            login()
        elif ch == 3:
            break
        else:
            print("Wrong Choice!")
start()