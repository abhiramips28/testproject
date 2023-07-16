def cust_login():
    email = str(input("Enter Your Email : "))
    password = str(input("Enter Your Password : "))

    if userExists(email, password):
       print("Welcome!")
    else:
        print("Sorry, Invalid Credentials!")

    name = str(input("Enter Your Name : "))
    phn_no = int(input("Enter Your Surname : "))
    email = str(input("Enter Your Email : "))
    password = str(input("Enter Your Password : "))
    confPassword = str(input("Confirm Your Password : "))

    if (password == confPassword):
        print("User Accepted!")
        user = createUser(name, phn_no, email, password)
    else:
        print("User Rejected! Invalid Password Combination")



cust_login()