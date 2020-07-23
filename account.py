class bank:
    sum=0
    x=int()
    def __init__(b,a,x,y):
     b.name=a
     b.salary=x
     b.age=y
    def deposit(b):
     b.a=int(input("enter the amount u want to deposit"))
     bank.sum=bank.sum+b.a
     print("your total balance is",bank.sum,"only")
    def withdrawl(b):
     b.a=int(input("enter amount u want to withdrawl"))
     bank.sum=bank.sum-b.a
     print("your total balance is",bank.sum,"only")
    def checkbalance():
     print("your  balance is",bank.sum,"only")
q=bank("rishav",9000,int(12))
b=int(input("press 1. for deposit money \npress 2. for withdraw money\npress 3. for checkbalance\n"))


     
     
        
        
