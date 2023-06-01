class Person:
    def __init__(self,name,dob,height):
        self.name=name
        self.dob=dob
        self.height=height

    def get_summary(self):
       print("your name is" +self.name+ "and your dob is" + self.dob + "and your height is" +self.height)



sivan=Person("Sivan","14 October 1999","6 feet")

sivan.get_summary()