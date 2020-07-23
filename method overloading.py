class marks:
    result =0
    

    def add(self,t=None,*args):
        if t=='int':
            self.result=0
        if t=='str':
            self.result=''
        for i in args:
            self.result=self.result+i
        return self.result
p=marks()
print(p.add('int',4,6,12,243))
print(p.add('str',"rishav","rapta"))
