class Person:
    def __init__(self,firstname,lname):
        self.firstname=firstname
        self.lname=lname

    def printname(self):
        print(self.firstname,self.lname)

x=Person("Sadman","Mehedi")
x.printname()

class