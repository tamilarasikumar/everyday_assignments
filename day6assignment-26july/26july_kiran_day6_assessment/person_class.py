class Person:
    def __init__(self,name):
        self.myname=name
    def sayMyName(self):
        print(self.myname)
n=input("enter a name:")
obj=Person(n)
obj.sayMyName()