class python:
    c=0
    def cal(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
    def view(self):
        print "a=",self.a
        print "b=",self.b
        print "c=",self.c
    def concat(self,x,y):
        self.x=x
        self.y=y
        return self.x+self.y
        
py=python()
a=input("enter a number: ")
b=input("enter another number: ")
py.cal(a,b)
py.view()
x=str(input("enter first name: "))
y=str(input("enter last name: "))
z=py.concat(x,y)
print "your name is: ",z
