class parent:
    def func(self,a,b):
        self.a=a
        self.b=b
    def view(self):
        print "this is super class"
        print "a=",self.a," and b=",self.b
class child (parent):
    def view(self):
        print "this is child class"
        print "a=",self.a," and b=",self.b
    def only(self):
        print "this is for only child class"
s=parent()
s.func(10,20)
s.view()      
c=child()
c.func(100,200)
c.view()
c.only()
print"Thank you"
