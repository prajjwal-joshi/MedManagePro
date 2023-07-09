import mysql.connector
import datetime
from tabulate import tabulate
mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="cpp_pharmacymanagementsystem"

)
mycursor=mydb.cursor()

mycursor.execute('''CREATE TABLE IF NOT EXISTS customer (
  cid int(5) PRIMARY KEY NOT NULL,
  cname varchar(20) NOT NULL,
  ContactNo int(10) NOT NULL,
  address varchar(30) NOT NULL)
 ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
mydb.commit()
mycursor.execute('''CREATE TABLE IF NOT EXISTS `admin` (`admn_id` INT(5) PRIMARY KEY NOT NULL , `name` VARCHAR(20) NOT NULL , `password` VARCHAR(20) NOT NULL ) ENGINE = InnoDB;

''')
mydb.commit()

mycursor.execute('''CREATE TABLE IF NOT EXISTS `medicine_tb` (
  `id` int(11) PRIMARY KEY NOT NULL,
  `name` varchar(50) NOT NULL DEFAULT '0',
  `company` varchar(50) NOT NULL DEFAULT '0',
  `arrival_date` date DEFAULT NULL,
  `expire_date` date NOT NULL,
  `price` float NOT NULL DEFAULT 0,
  `quantity` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
''')
mydb.commit()
# mycursor.execute('''insert into admin(admn_id,name,password) values(1502,'prajjwal','prajjwal')''')
# mydb.commit()
# mycursor.execute('''INSERT INTO `medicine_tb` (`id`, `name`, `company`, `arrival_date`, `expire_date`, `price`, `quantity`) VALUES
# (1, 'Cardipro - 50', 'Square LTD.', '2020-12-11', '2023-12-30', 60, 16);''')
mydb.commit()
def BuyMedicine():
    mycursor.execute("select * from medicine_tb")
    med=mycursor.fetchall()
    
    print(tabulate(med,headers=['id' , 'name', 'company' ,'arrival_date' ,'expiry_date' ,'price' ,'quantity']))
    
    id=int(input("Enter medicine id : "))
    name=str(input("Enter name of medicine : "))
    sc=("select quantity from medicine_tb where id=%s")
    bc=(id,)
    mycursor.execute(sc,bc)
    qt=mycursor.fetchone()
    if(qt[0]>0):
        print("You can buy this medicine ")
        
        ch=str(input("Do you want to buy or not? y/n "))
        if((ch=="y")or(ch=="Y")): 
            qty=int(input("Enter the quantity : "))
            print("You have successfully purchased your medicine ")
            s2="select price from medicine_tb where id=%s"
            b2=(id,)
            mycursor.execute(s2,b2)
            price=(mycursor.fetchone())[0]
            print("Price = ",qty*price)
            s1="update medicine_tb set quantity = quantity - %s where id=%s"
            b1=(qty,id)
            mycursor.execute(s1,b1)
        else:
            return
    else:
        print("Medicine out of stock ")

def ShowItemList():
    mycursor.execute("select * from medicine_tb")
    med=mycursor.fetchall()
    
    print(tabulate(med,headers=['id' , 'name', 'company' ,'arrival_date' ,'expire_date' ,'price' ,'quantity']))
def FindItemFromList():
    ch="y"
    while(ch=="y"):
        name=str(input("Enter medicine name: "))
        s1='''select * from medicine_tb where name like "%'''+name+'''%" '''
        mycursor.execute(s1)
        md=mycursor.fetchall()
        print(tabulate(md,headers=['id' , 'name', 'company' ,'arrival_date' ,'expire_date' ,'price' ,'quantity']))
        ch=input("do you want to search more medicine?(y/n) :")
    
def AddIteminStock():
       ch="y"
       while(ch=='y'):
        id=int(input("Enter Id : "))
        name=input("Enter medicine name : ")
        company=input("Enter company name : ")
        expiry_year = int(input('Enter expiry year: '))
        expiry_month = int(input('Enter expiry month: '))
        expiry_day = int(input('Enter expiry day: '))
        expiry_date = datetime.date(expiry_year, expiry_month, expiry_day)
        price=float(input("Enter price of medicine : "))
        qty=int(input("Enter the medicine quantity: "))
        s='''insert into medicine_tb (id,name,company,expire_date,price,quantity) values(%s,%s,%s,%s,%s,%s)'''
        b=(id, name, company, expiry_date, price, qty)
        try:
            mycursor.execute(s,b)
            mydb.commit()
            print("Record added successfully ")
            
        except: 
            print("Error entering data ")
        ch=input("Do you want to enter more data?(y/n) : ")
def UpdateStockItem():
    mycursor.execute("select * from medicine_tb")
    med=mycursor.fetchall()
    
    print(tabulate(med,headers=['id' , 'name', 'company' ,'arrival_date' ,'expire_date' ,'price' ,'quantity']))
    id=int(input("Enter Id of medicine you want to update : "))
    s='''select id from medicine_tb'''
    mycursor.execute()
    md=mycursor.fetchall()
    do=id in md
    if(do):
        name=input("Enter medicine name : ")
        company=input("Enter company name : ")
        expiry_year = int(input('Enter expiry year: '))
        expiry_month = int(input('Enter expiry month: '))
        expiry_day = int(input('Enter expiry day: '))
        expiry_date = datetime.date(expiry_year, expiry_month, expiry_day)
        price=float(input("Enter price of medicine : "))
        qty=int(input("Enter the medicine quantity: "))
        
        b0=(name, company, expiry_date, price, qty)
        s0='''update medicine_tb set name=%s, company=%s, expire_date= %s, price=%s, quantity=%s'''
        try:
            mycursor.execute(s0,b0)
            mydb.commit()
            print("Record updated successfully")
        except:
            print("Record is not updated try again")
    else:
        print("ID does not exist")
def DeleteStockItem():
    mycursor.execute("select * from medicine_tb")
    med=mycursor.fetchall()
    
    print(tabulate(med,headers=['id' , 'name', 'company' ,'arrival_date' ,'expire_date' ,'price' ,'quantity']))
    id=int(input("Enter Id of medicine you want to update : "))
    s='''select id from medicine_tb'''
    mycursor.execute()
    md=mycursor.fetchall()
    do=id in md
    if(do):
        s0='''delete from medicine_tb where id=%s'''
        b0=(id,)
        try:
            mycursor.execute(s0,b0)
            mydb.commit()
            print("Data deleted successfully")
        except:
            print("Item could not be deleted")

flag=True
def admin():
    flag1=True
    while(flag1==True):
    
        print('''
       
        1.ShowItemList
        2.FindItemFromList
        3.AddIteminStock
        4.UpdateStockItem
        5.DeleteStockItem
        6.Exit
        ''')
        choice = int(input("Enter choice: "))
        
        if(choice==1):
            ShowItemList()
        elif(choice==2):
            FindItemFromList()
        elif(choice==3):
            AddIteminStock()
        elif(choice==4):
            UpdateStockItem()
        elif(choice==5):
            DeleteStockItem()
        elif(choice==6):
            flag1=False
        else:
            print("You have entered wrong input")
def customer():
    cid=int(input("Enter your id number : "))
    name=input("Enter your name: ")
    contactno=int(input("Enter your contact number : "))
    address=input("Enter your address : ")
    s0='''insert into customer(cid, cname, ContactNo, address) values(%s,%s,%s,%s)'''
    b0=(cid,name,contactno,address)
    try:
        mycursor.execute(s0,b0)
        mydb.commit()

        flag1=True
        while(flag1==True):
            print(''' 
            1.BuyMedicine(
            2.ShowItemList()
            3.FindItemList()
            4.Exit'''
            )
            ch=int(input("Enter choice: "))
            if(ch==1):
                BuyMedicine()
            elif(ch==2):
                ShowItemList()
            elif(ch==3):
                FindItemFromList()
            elif(ch==4):
                flag1=False
            else:
                print("Wrong input ")
    except:
        print("error try again ")

while flag:        
    inp1 = int(input("Who are you: \n 1) Admin \n 2) Customer \n 3)Exit\n"))
    if(inp1 == 1):
        inp2 = input("Enter admin id: ")
        inp7 = input("Enter password: ")
        sp = '''select password from admin where admn_id = %s'''
        bp = (inp2,)
        try:
            mycursor.execute(sp,bp)
            xv = mycursor.fetchone()
            if(inp7 == xv[0]):
                admin()
            else:
                ("Sorry wrong input")
        except:
            print("error")
    elif (inp1 == 2):
        customer()
    elif (inp1 == 3):
        flag = False
