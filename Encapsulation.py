
class Student:
    def __init__(self,name,id):
        self.name=name
        self.__id=id

    def details(self):
        print(f"His name is {self.name} and id is {self.__id}")
        self.__id()


    def __id(self):
        print("Private Method is run")


Sivan=Student("Sivan","43")

Sivan.details()