"""defaultid = "admin"
defaultpassword = "1234"

userid = input("User id : ")
if userid != defaultid:
    print("your id not found")
else:
    userpassword = input("Password : ")
    if userpassword != defaultpassword:
        print("ID or Password is wrong!")
    else:
        print("Login! Welcome")

userid = input("User id : ")
userpassword = input("Password : ")
if userid == defaultid and userpassword == defaultpassword :
    print("Login! Welcome")
else:
    print("fail! ID or Password is wrong!")

age = int(input())
if (age < 15):
    print("ยุวชน")
    print("เยาวชน")
elif (age <= 25):
    print("ใผู้หญ่")
elif (age < 60):
else:
    print("สูงอายุ")"""


"""victory = 20
x = 0
while x != victory:
    x = int(input("Guess number : "))
    if x > victory:
        print("ตัวเลขมากไป")
    elif x < victory:
        print("ตัวเลขน้อยไป")
    elif x == victory:
        print("Victory! you win")"""


"""defaultid = "admin"
defaultpassword = "1234"
usderid = ""
userpassword = ""

while usderid != defaultid and userpassword != defaultpassword:
    usderid = input("User ID : ")
    userpassword = input("User Password : ")
    if usderid != defaultid and userpassword != defaultpassword:
        print("Your ID or password is wrong , Please try agian")
    elif usderid == defaultid and userpassword == defaultpassword:
        print("Login! Welcome")

userid = input("User Id : ")
userpassword = input("User Password : ")
while userid != "admin" or userpassword != "1234":
    userid = input("User Id : ")
    userpassword = input("User Password : ")
print("DONE")


for x in range(int(input("Input number : "))):
    x += 1
    for y in range(12):
        y += 1
        print(x,"*",y,"=",x*y)

for y in range(12):
    if (y+1)%2 == 0:
        continue
    for x in range(12):
        print(y+1, "x", x + 1, "=", (y+1) * (x + 1))

n = int(input("กรอกตัวเลขมา : "))
print(n)
for m in range(n):
    print("*"*(m+1))

x = int(input("Input number : "))
for n in range(x):
    n = 1+2*n
    x -= 1
    print((" "*x)+(n*"*"))

a = 5
for b in range(a):
    print(b,end="-")




def vatCalculator():
    x = int(input("Total price (THB) : "))
    result = "Included vat7% : "+str(int(x+(x*7/100)))+" THB"
    return result

print(vatCalculator())

def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Login! Welcome")
        showMenu()
    else:
        print("Fail, Please try agian!")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        print(vatCalculator(int(input("Vat : " ))))
        print(priceCalculator())

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()"""
x=1
y=1
while True:
    product = {}
    product["Product"+str(x)] = input("พิมพ์สินค้าของคุณ : ")
    product["values"+str(y)] = input("พิมพ์ราคาสินค้า : ")
    x += 1
    y += 1
    print(product)







