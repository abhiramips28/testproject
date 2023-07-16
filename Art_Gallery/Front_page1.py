import mysql.connector

from sketchpy import library as lib
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
            from customer_signup_login import start
            start()
            f()
            choice = int(input("ENTER THE CHOICE:"))
        if choice == 4:
            from drawing import draw
            f()
            choice = int(input("ENTER THE CHOICE:"))
        if choice == 5:
            from compitation import play
            f()
            choice = int(input("ENTER THE CHOICE:"))

start()

