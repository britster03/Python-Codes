from datetime import date 
#import random
class store:
    def __init__(self,name,price,id):
        self.name = name
        self.price = price
        self.id = id
print()
BAT = store("SG BAT",7000,"SG1")
BALL = store("SG BALL",1500,"SG3")
JERSEY = store("JERSEY",700,"JS3")
HELMET = store("HELMET",670,"HL9")
lst = [BAT,BALL,JERSEY,HELMET]
a = 1
print("\t\t\t\t\t\t\t    *-*-*-*-ITEMS-*-*-*-*")
print("\t\t\t\t\t\t\t| Item \t         |  Price     |")
print("\t\t\t\t\t\t\t------------------------------")
for i in lst:
    print(f"\t\t\t\t\t\t\t| {i.name}\t | {i.price}\t    |" )
    a = a + 1
print("\t\t\t\t\t\t\t------------------------------")
print()
quantity = []
for i in lst:
    print(f"\t\t\t\t\t\tEnter quantity of {i.name} you want:")
    inp = int(input("\t\t\t\t\t\t---> "))
    quantity.append(inp)
print()
a = 0
finalBill = []
for i in lst:
    bill = i.price * quantity[a]
    finalBill.append(bill)
    a = a + 1
today= date.today()
d1 = today.strftime("%d/%m/%y")    
Bill = 0
for i in range(len(finalBill)):
    Bill = Bill + finalBill[i] 
#num = random.randint(100,1000)
print("---------------------------------------------------------")
print(f"\t\t\t\t\t\t----------------(DATE:{d1})-----------------")
print("\t\t\t\t\t\t-*-*-*-*-*-*-*-TOTAL INVOICE-*-*-*-*-*-*-*-*-")
print("\t\t\t\t\t\t| Name\t        | ID |   Price | Quantity |")
print("\t\t\t\t\t\t-------------------------------------------")
a = 0
for i in lst:
        if(quantity[a]!=0):
            print(f"\t\t\t\t\t\t| {i.name}\t| {i.id}\t| {i.price}\t| {quantity[a]}\t   |")
        a = a + 1
print("\t\t\t\t\t\t--------------------------------------------")
print(f"\t\t\t\t\t\tFinal Total: {Bill}")
print("\t\t\t\t\t\t--------------------------------------------")