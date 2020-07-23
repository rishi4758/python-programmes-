dec={}
for i in range(1,16):
 dec[i]=i*i*i
print(dec)
while i<16:
 a=int(input("eneter the key"))
 if dec[i]==i*i*i:
    
    print("keu is already prest in a dictionary")
    continue
 else :
    b=int(input("enter the value for the key"))
    dec[i]=b;
    break
