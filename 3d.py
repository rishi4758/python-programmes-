class a:
    def __init__(b,o,l,k):
        b.x=o
        b.y=l
        b.z=k
    def __add__(p,q):
        return (p.x+q.x,p.y+q.y,p.z+q.z)
    def __str__(k):
        return '(%d,%d,%d)'%(k.x,k.y,k.z)
v1=a(4,5,6)
v2=a(7,8,9)
v3=v1+v2
print(v3)
