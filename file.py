f1=open("rishav.txt")
f3=f1.read()
f2=f3.split()
for x in range(len(f2)):
    b=f2[x]
    if b[0]=='u':
        print(b)
    else:
        continue
