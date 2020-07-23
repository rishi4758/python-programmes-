f1=open("lok.txt","r");

f2=open("bo.txt","w");
i=0;
while i<100:
    x=f1.read(1);
    if x==" ":
     continue;
    else:
     y=x;
     f2.write(y);
    i=i+1;
    
f1.close();
f2.close();    
