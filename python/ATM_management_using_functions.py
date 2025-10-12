def deposite():
    a = int(input("enter a amount:"))
    if a>0:
        print(str(a)+" is credited successfully")
        return a
    else:
        print("invalid balance.Please enter amount greater than zero.")
        return 0
def withdraw(amount):
    a = int(input("Enter amount: "))
    if a<=amount:
        print(str(a)+" is debited successfully!")
        amount-=a
        return a
    else:
        print("Insufficient Balance")
        return 0
def check_balance(amount):
    return "current balance is "+str(amount)
pin = 1234
amount = 0
p = int(input("enter pin: "))
if p==pin:
    while True:
        print("1) deposite")
        print("2) withdraw")
        print("3)check balance")
        print("4) exit")
        opt = int(input("choose one option: "))
        if opt ==1:
            amount+=deposite()
        elif opt ==2:
            amount-=withdraw(amount)
        elif opt==3:
            print(check_balance(amount))
        elif opt==4:
            print("Thanks for visiting.")
            break
        else:
            print("enter the valid pin.")