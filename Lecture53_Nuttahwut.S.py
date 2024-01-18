def vatCalculator():
    x = int(input("Total price (THB) : "))
    result = "Included vat7% : "+str(int(x+(x*7/100)))+" THB"
    return result

print(vatCalculator())