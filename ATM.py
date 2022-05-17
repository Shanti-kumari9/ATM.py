language=input("language ")
print("welcome to indian overseas bank")
secretpin=input("enter the 4 digits pin code")
if secretpin=="4667":
    user_choose=input("withdrawl or balance enquiry or deposite")
    balance=10000
    if user_choose=="w":
        amount=int(input("enter the amount"))
        if amount <=5000:
            print("processing")
            print("transfer complet")
            print(balance-amount,"left balance")
        else:
            print("cannot be withdraw")
    if user_choose=="balance enquiry":
        print("your current balance is",balance)
    if user_choose=="deposite":
        deposite=int(input("enter the deposite amount"))
        print(deposite+10000,"is your current balance")
    else:
        print("thankq")
        print("thank for visiting indian overseas bank")