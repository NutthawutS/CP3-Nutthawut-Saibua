userID = input("Plese enter your ID : ")
userPassword = input("Plese enter your Password : ")
if userID == "admin" and userPassword == "1234":
        print ("----------------Welcome to mobile shop-----------------")
        print ("===================================================")
        print ("S1 << Samsung Note 10+ - Black     Price 9,999 THB")
        print ("S2 << Samsung Note 10+ - White     Price 9,999 THB")
        addToCart = input("Please enter Item ID that you want to purchase : ")
        if addToCart == "S1":
                quantity = int(input("How many pieces do you want? : "))
                totaltransaction = 9999*quantity
                accepts1 = input ("No exchange or refund Confirm Y or N? : ")
                if accepts1 == "Y" :
                        print ("Total :",totaltransaction,"THB")
                if accepts1 == "N":
                        print ("order canceled, please try again")
        elif addToCart == "S2":
                quantity = int(input("How many pieces do you want? : "))
                totaltransaction = 9999*quantity
                accepts2 = input("No exchange or refund Confirm Y or N? : ")
                if accepts2 == "Y" :
                        print ("Total :",totaltransaction,"THB")
                if accepts2 == "N":
                        print ("order canceled, please try again")

