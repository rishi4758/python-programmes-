class marks:
    def add(self,t=None,*args):
        if t is not None:
            print('hello'+t)
        else:
            print('no argumentss')
p=marks()
print(p.add())
print(p.add('rishav'))
