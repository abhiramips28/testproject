import mysql.connector


mydb=mysql.connector.connect(host='localhost',user='root',password='abhirami')
# print(mydb)

mycursor=mydb.cursor()

def search():
    A = str(input(">>>>>>>>>>>"))
    s=A.upper()
    mycursor.execute("use art_gallery")
    mycursor.execute("select * from artist_sell")
    myresult = mycursor.fetchall()

    d={1:'id_no',2:'user_name',3:'password',4:'painting_name',5:'mediam',6:'size',7:'price',8:'art_code',9:'contact_no',10:'gmail'}

    dict={}
    t=0
    none = 1
    for i in myresult:
        for x in i:
            # print(x)
            t=t+1
            dict.setdefault(d.get(t),x)
        # print(dict)
        c=dict.get('painting_name')
        c=c.upper()
        if s==c or s in c :
            none=0
            row = 6
            for i in range(row):
                for j in range(row):
                    print("****", end="")
                if i==0:
                    print("  ",c,end="")
                if i==1:
                    print("   By",dict.get('user_name'),end='')
                if i==2:
                    print("   ----------------------------------------",end='')
                if i==3:
                    print("     Size           Medium         Art Code",end='')
                if i == 4:
                     print("  ",dict.get('size')," ",dict.get('medium')," ",dict.get('art_code'), end='')
                if i==5:
                    print("   ----------------------------------------",end='')
                print()
            print("                           Rs ",dict.get('price'),"                    ","Buy Now")
            print("                           Delivery time: 5-7 business days")
            print('\n')
        dict={}
        t=0

    if none==1:
        print("No Records Found")

search()