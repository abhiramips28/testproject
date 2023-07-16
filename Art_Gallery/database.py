import mysql.connector

# mysql-python connector
mydb = mysql.connector.connect(host='localhost', user='root', password='abhirami',database='art_gallery')
# print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE Art_Gallery")

mycursor.execute("use art_gallery")

# mycursor.execute("create table customer(id int NOT NULL AUTO_INCREMENT  PRIMARY KEY, cust_name varchar(250), GMAIL varchar(250), PASSWORD varchar(250), MOBILE_NUMBER int);")

# mycursor.execute("create table artist(id_no int NOT NULL AUTO_INCREMENT PRIMARY KEY, user_name varchar(25),password varchar(25),contact_no int,gmail varchar(25), location varchar(25),about varchar(25));")

# mycursor.execute("create table cust_card(id_no int NOT NULL AUTO_INCREMENT PRIMARY KEY,cust_gmail varchar(25),cust_password varchar(25),cust_name varchar(25), artist_pwd varchar(25),artist_gmail varchar(25), painting_name varchar(25),mediam varchar(30),size varchar(30),price int,payment_ststs varchar(20),artist_name varchar(25));")

# mycursor.execute("create table buy(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,painting_name varchar(200), artist_name varchar(25),user_name varchar(30),state varchar(30),district varchar(30),address varchar(30),pin_code int,mob_num int);")
# mycursor.execute("ALTER TABLE buy MODIFY mob_num BIGINT")
# mycursor.execute("create table artist_sell(id_no int NOT NULL AUTO_INCREMENT PRIMARY KEY, gmail varchar(25),password varchar(30),painting_name varchar(30),mediam varchar(30),size varchar(20) ,price int,art_code varchar(30),sell_or_not varchar(30),user_name varchar(30));")



# mycursor.execute("ALTER TABLE customer MODIFY MOBILE_NUMBER BIGINT")
# sql = "INSERT INTO customer(id,cust_name,GMAIL,PASSWORD,MOBILE_NUMBER) VALUES (%s,%s,%s,%s,%s)"
# val = [
#     (1,'janaki','janaki001@gmail.com','janaki25',9895736475),
#     (2,'manoj','manoj2@gmail.com','manojk5',9973746251),
#     (3,'varma','varma201@gmail.com','varma0010',9875646650),
#     (4,'Muhammed','muhammed8@gmail.com','muhammed66',7052435210),
#     (5,'lekha','lekha75@gmail.com','lekha1002',9847635241),
#     (6,'meghana','meghana5@gmail.com','meg5hana',8547845312),
#     (7,'jerin','jerinj01@gmail.com','jerinm202',9684635214),
#     ]
# mycursor.executemany(sql,val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted")

# mycursor.execute("ALTER TABLE artist MODIFY contact_no BIGINT")
# mycursor.execute(("ALTER TABLE artist MODIFY column about varchar(600)"))
#
# #insert rows into the table
# sql = "INSERT INTO artist(id_no,user_name,password,contact_no,gmail,location,about) VALUES (%s,%s,%s,%s,%s,%s,%s)"
# val = [
# (1,'sanjay','sanju123@',7045025310,'sanjusanjay23@gmail.com','kannur,kerala','creates realistic paintings personifying the character of Kolkata, India. Best known for his portrait series of the late Prime Minister Rajiv Gandhi,the artist depicts Gandhi in interior scenes that are striking and ambiguous as…'),
# (2,'shamendu sonavane','shammu@172',6238420162,'shamendu12@gmail.com','Coimbatore,Tamlinadu','An artist, known for his brilliant portrayal of nature, has been painting nature at its vivid best for last several years.'),
# (3,'Rajan Raghavan','rajan@142',8802437214,'rajrajan12@gmail.com','Thrissur,kerala','paints in themes which express relationships between humans and animals. Showing contemporary abstracts using a bright palette is what he loves.'),
# (4,'ganapati hegda','ganapathi12@',9874302243,'ganapathi34@gmail.com','Bengaluru,karnataka','Explore the paintings by Ganapati Hegde, a contemporary Indian painter known for his unique blend of traditional and modern techniques.'),
# (5,'Punekar','punness21@',8864534531,'punekae99@gmail.com','pune,Maharashtra','have never thought only about pune he taught of all over india so he is famous for his bravery and thinking.'),
# (6,'sanjay chakrabarty','sanju09@',9962510234,'sanjusanju@gmail.com','Trivandrum kerala','wields a spatula with a flourish to paint some inspired and spectacular images of the holy Banaras City.'),
# (7,'Dipti kumar','dipti88@',6254120321,'dipti66@gmail.com','kollam kerala','creating personalized gifts like calendars and caricatures. Her creations can surely make one smile while conveying a message to the masses.'),
# (8,'ghanshyam gupta','ghan23@',9965021304,'ghanshyam44@gmail.com','Mathura Uttar Pradesh','painter who has the rare honour of exhibiting his creations along with the some of the greatest artists of all times: Lucian Freud, Pablo Picasso, Paul Cezanne, Edward Munch, Henri Matisse, Rembrandt, and Albert Durer.'),
# (9,'ghanshyam nayak','ghan23@32',9582341523,'nayakghana@gmail.com','Mathura,Jharkhand',"appeared as a child artist in a popular Bollywood song 'Nani Teri Morni ko Mor Le Gye' along with Farhan Akhtar's mother Honey Irani."),
# (10,'Rajan','rajraj@12',9546281320,'rajraj23@gmail.com','Kozhikode,Kerala','Searching for top portrait painting artist in India for celebrities and famous personalities at economical price, enquire now at Rajan 2023-24.'),
# (11,'Paras','paras@23',9986521420,'paraspp23@gmail.com','Nalgonda,Telangana','paints in themes which express relationships between humans and animals. Showing contemporary abstracts using a bright palette is what he loves.'),
# (12,'suresh','susu@01',9982531023,'sureshsuresh12@gmail.com','Alappuzha,Kerala','rich heritage of association with the pichvai tradition, tracing his family lineage back to the first five artists who accompanied.'),
# (13,'Ganapathi hega','ganahana@12',9963254172,'ganapathi45@gmail.com','Krishna, Andhra Pradesh','Buy artworks directly of artist Ganapati Hegde artworks with Authenticity certificate. Worldwide Shipping.'),
# (14,'Bhasker chitrakar','babu@123',9573548241,'babu123@gmail.com','Chennai,Tamil Nadu','painters from an artisan community in West Bengal,practicing Kalighat painting since the 19th century. work upholds classical technique,first to bring visions of contemporary society into this traditional art.'),
# (15,'Govind Dumbra','govi@123',7382645312,'govind123@gmail.com','Agra,Uttar Pradesh','loves painting mainly the scenes of rainy rural India.'),
# ]
#
# mycursor.executemany(sql,val)
#
# mydb.commit()

# mycursor.execute("use art_gallery")
# sql = "INSERT INTO artist_sell(id_no,gmail,password,painting_name,mediam,size,price,art_code,sell_or_not,user_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#
# val = [
#     (1,'sanjusanjay23@gmail.com','sanju123@','Abstract','crylic on canvas','36*59 inches',165000,'DD08','SELL','sanjay'),
#     (2,'shamendu12@gmail.com','shammu@172','Seascape','acrylic on canvas','16*16 inches',450000,'EE09','NOT SELL','shamendu sonavane'),
#     (3,'rajrajan12@gmail.com','rajan@142','Abstract','acrylic on canvas','8*8 inches',554250,'QW78','SELL','Rajan Raghavan'),
#     (4,'ganapathi34@gmail.com','ganapathi12@','Ganesha','Oil on canvas','24*24inches',4100000,'TR76','SELL','ganapati hegda'),
#     (5,'punekae99@gmail.com','punness21@','Tantric abstract','acrylic on canvas','36*36 inches',5420100,'GG45','SELL','Punekar'),
#     (6,'sanjusanju@gmail.com','sanju09@','reflection','acrylic on canvas','13*14 inches',63200,'FH66','NOT SELL','sanjay chakrabarty'),
#     (7,'dipti66@gmail.com','dipti88@','maharaas','Oil on canvas','24*24 inches',452000,'AD33','NOT SELL','Dipti kumar'),
#     (8,'ghanshyam44@gmail.com','ghan23@','meditation','acrylic on canvas','8*8 inches',54200,'AQ23','NOT SELL','ghanshyam gupta'),
#     (9,'nayakghana@gmail.com','ghan23@32','villege','acrylic on canvas','8*8 inches',4320000,'AS34','NOT SELL','ghanshyam nayak'),
#     (10,'rajraj23@gmail.com','rajraj@12','Floral abstract','acrylic on canvas','12*12 inches',243000,'SQ34','NOT SELL','Rajan'),
#     (11,'paraspp23@gmail.com','paras@23','Musical Ganesha','acrylic on canvas','36*12 inches',220000,'RT44','SELL','Paras'),
#     (12,'sureshsuresh12@gmail.com','susu@01','cityscope','acrylic on canvas','30*60 inches',124000,'ER90','NOT SELL','suresh'),
#     (13,'ganapathi45@gmail.com','ganahana@12','saraswati','Oil on canvas','12*12 inches',100000,'US23','SELL','Ganapathi hega'),
#     (14,'babu123@gmail.com','babu@123','babu-bibi in an auto','mixed media on paper','15*11 inches',42000,'RR45','NOT SELL','Bhasker chitrakar'),
#     (15,'govind123@gmail.com','govi@123','Banaras Ghat','acrylic on canvas','24*36 inches',55000,'TR43','SELL','Govind Dumbra'),
#     ]
#
# mycursor.executemany(sql,val)
#
# mydb.commit()


# mycursor.execute("drop table cust_card")


# sql = "insert into cust_card(id_no,cust_gmail,cust_password,cust_name,artist_pwd,artist_gmail,painting_name,mediam,size,price,payment_ststs,artist_name) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# val =[
#     (1,'janaki001@gmail.com','janaki25','Janaki','sanju123@','sanjusanjay23@gmail.com','Abstract','acrylic on canvas','36*59 inches',165000,'PAID','sanjay'),
#     (2,'manoj2@gmail.com','manojk5','Manoj','rajan@142','rajrajan12@gmail.com','Abstract','acrylic on canvas','8*8 inches',554250,'PAID','Rajan Raghavan'),
#     (3,'varma201@gmail.com','varma0010','Varma','ganapathi12@','ganapathi34@gmail.com','Ganesha','Oil on canvas','24*24inches',4100000,'PAID','ganapati hegda'),
#     (4,'muhammed8@gmail.com','muhammed66','Muhammed','punness21@','punekae99@gmail.com','Tantric abstract','acrylic on canvas','36*36 inches',5420100,'PAID','Punekar'),
#     (5,'lekha75@gmail.com','lekha1002','Lekha','paras@23','paraspp23@gmail.com','Musical Ganesha','acrylic on canvas','36*12 inches',220000,'PAID','Paras'),
#     (6,'meghana5@gmail.com','meg5hana','Meghana','ganahana@12','ganapathi45@gmail.com','saraswati','Oil on canvas','12*12 inches',100000,'PAID','Ganapathi hega'),
#     (7,'jerinj01@gmail.com','jerinm202','Jerin','govi@123','govind123@gmail.com','Banaras Ghat','acrylic on canvas','24*36 inches',55000,'PAID','Govind Dumbra'),
#
# ]
# mycursor.executemany(sql,val)
#
# mydb.commit()

