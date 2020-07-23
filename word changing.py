
def language(a):
 b=""
 for i in a:
   if i.lower() in "aeiou":
     if i.isupper():
           b=b+"G"
     else:      
           b=b+"g"
   else:
     b=b+i
 return b;

print(language(input("enter word")))
