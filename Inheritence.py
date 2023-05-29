class Person:
    def __init__(self,firstname,lname):
        self.firstname=firstname
        self.lname=lname

    def printname(self):
        print(self.firstname,self.lname)


x=Person("Sadman","Mehedi")
x.printname()


#By using Person init i will still be able to access the parent class's initiate function

class Student(Person):
    def __init__(self,fname,lname,year):
        #Person.__init__(self,fname,lname)
        #We can also do by using the Super Function
        super().__init__(fname,lname)
        self.graduationyear=year

    def welcome(self):
        print("Welcome", self.firstname, self.lname, "to the class of", self.graduationyear)



y=Student("Anam"," Raz",2023)
print(y.welcome())

