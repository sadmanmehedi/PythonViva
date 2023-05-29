class MyClass:
    x=17

p1=MyClass()
print(p1.x)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return  f"{self.name}({self.age})"

p1=Person("Sivan",23)



print(p1)


class Draft:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello Hunny Bunny MRS."+self.name+" MEHEDI Aged"+str(self.age)+" years OLD")



s1=Draft("ANAM",21)
print(s1.myfunc())

class Test:
    def __init__(self,names,id):
        self.names=names
        self.id=id

    def myF(self):
        print("Hey There!"+self.names+"ID: "+str(self.id))


x=Test("SADMAN",43)
x.id=17
print(x.id)
del x.id
#print(x.id)
del x
#print(x.id)