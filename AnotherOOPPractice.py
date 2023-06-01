class Cousins:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob

    def setname(self, newname):
        self.name = newname

    def setdob(self,newdob):
        self.dob=newdob

    def bdates(self):
        return

c1=Cousins("Tonmoy",1994)
c2=Cousins("Ifty",1994)
c3=Cousins("Tonmoy",1994)

c3.setdob(1880)
c3.setname("Aditto")

list=[]

list.append(c1)
list.append(c2)
list.append(c3)


print(list[2].name)