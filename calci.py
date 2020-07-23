w="rishab"
q=input()
c=3;
d=False
f=0
while q!=w and not(d):
   if f<c:
    q=input("enter the word again")
    f=f+1
   else:
       d=True
if d==True :
 print("u lost it")
else:
 print("u win this")

    
