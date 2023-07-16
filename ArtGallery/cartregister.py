def CartRegister():

       print("$$$$$$$$$$$$ REGISTER $$$$$$$$$$$$")
       custName = input("NAME: ")
       custAdderss = input("Address:  ")
       phn_no = int(input("MOBILE NUMBER: "))
       pin_code = int(input("PINCODE: "))
       if custName.isalpha() == True or " " in custName:
          if custAdderss.isalpha() == True or " " in custAdderss:
             if type(phn_no)==int and len(str(phn_no))==10:
                if type(pin_code)==int:
                       with open("cart_register_details.txt", 'w+') as fp:
                              for i in fp:
                                  if x in i:
                                     print("This account already exists")
                                     CartRegister()
                              else:
                                  with open("cart_register_details.txt", "r") as f:
                                    f.write(x)
                                    print(" you have successfully registered")
                                    print("\n")
                                    CartRegister()
                else:
                     print("invalid code")
                     print("\n")
                     CartRegister()
             else:
                 print("invalid number")
                 print("\n")
                 CartRegister()

          else:
              print("invalid address")
              print("\n")
              CartRegister()
       else:
           print("invalid name")
           print("\n")
           CartRegister()

CartRegister()


