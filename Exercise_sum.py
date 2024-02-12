menuList = []
priceList = []

def showBill():
    print("---- My Food----")
    price = 0
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        price += int(priceList[number])
    print("total price: ", price, "THB")

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()