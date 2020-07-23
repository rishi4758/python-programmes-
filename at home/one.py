from random import *;

a=(1,2,3,4);
b=list(a);
c=tuple(b);
print(b);
#tuple can be converted to list and vice versa where as string can be converted to list
#but there is no direct functtion to covert list into string we have to use ''.join(list_variable) for conversion of list to string
# swqap technique
def swap(a,b):
    return b,a;
x=5;
y=6;
print(swap(x,y));
#use of random function
i=0;
while i<6:
    print(random());
    i=i+1;
# concatenation of different datatype
c1=(3,4,5,"rishav");
c2=(8,5,6,'k');
print(c1+c2);


#dictionary- all is samw like list ,tuple but here instead of numeric index a=we can assign our own index that is also called key
#they are immutable
c4={};
print(type(c4));

c5={'1':"rishav",'ele':"1234","4":"12dsodn"};
print(c5['ele']);
c6=list(c5);
print(c6);
# to cone=vert list into dict not possible where as to convert dict into list possible but in list only keys of dictionary will be available not value of the key
