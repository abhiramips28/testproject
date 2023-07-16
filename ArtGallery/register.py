# def buy():
#
#     name = str(input("Name : "))
#     phone_number = int(input("PHONE NUMBER : "))
#     address = input("ADDRESS : ")
#     pincode = int(input("PINCODE : ")
#
#



# def Register():
#     Database()
#     if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
#         lbl_result2.config(text="Please complete the required field!", fg="orange")
#     else:
#         cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
#         if cursor.fetchone() is not None:
#             lbl_result2.config(text="Username is already taken", fg="red")
#         else:
#             cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
#             conn.commit()
#             USERNAME.set("")
#             PASSWORD.set("")
#             FIRSTNAME.set("")
#             LASTNAME.set("")
#             lbl_result2.config(text="Successfully Created!", fg="black")
#         cursor.close()
#         conn.close()