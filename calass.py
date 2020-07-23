class bank:
    sec=0
    def __init__(a,x,y):
     a.name=x
     a.age=y
     bank.sec+=1
     #here we are using class variable to update it wec need claassname.variaable
    def disp(a):
     print(a.name)
     print(a.age)
     print(bank.sec)
k=bank("rrtt","98")
k.disp()
l=bank("ahgsg","354")
l.disp()
m=bank("kjshkj","8")
m.disp()
#name age salary define 4 funcn they are  withdrawl deposit mini statement check balamncr
