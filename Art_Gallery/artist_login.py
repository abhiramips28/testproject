import mysql.connector

import cv2

mydb = mysql.connector.connect(host='localhost', user='root', password='abhirami')
# print(mydb)

from art_page2 import f

mycursor = mydb.cursor()

def start():
    l=1
    for l in range(0,3):
        choice = int(input("ENTER THE CHOICE:"))
        if choice == 1:
            from artist_search import search
            search()
            f()
            # x=input("press space and enter button to go home page")
        if choice == 2:
            from artist_signup_login import start
            start()
            f()
            choice = int(input("ENTER THE CHOICE:"))
        if choice == 3:
            print("1-LOGIN")
            print("2-REGISTER")
            c = int(input("ENTER THE CHOICE:"))
            while c < 3:
                if c == 1:
                    name = str(input("USER NAME:"))
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
                        print("registration compeleted ")
                        break
            f()
            choice = int(input("ENTER THE CHOICE:"))
        if choice == 4:
            p = input("upload the image")
            # import cv2
            image = cv2.imread(
                r'C:\Users\LENOVO\PycharmProjects\MiniProject\Art_Gallery\img.jpg')  # loads an image from the specified file
            # convert an image from one color space to another
            grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            invert = cv2.bitwise_not(grey_img)  # helps in masking of the image
            # sharp edges in images are smoothed while minimizing too much blurring
            blur = cv2.GaussianBlur(invert, (21, 21), 0)
            invertedblur = cv2.bitwise_not(blur)
            sketch = cv2.divide(grey_img, invertedblur, scale=158.0)
            cv2.imwrite("sketch.png", sketch)  # converted image is saved as mentioned name

            f()
choice = int(input("ENTER THE CHOICE:"))
f()

