
class Student:
    def __init__(self,name,id):
        self.name=name
        self.__id=id

    def __id2(self):
        print("Private Method is run")
    def details(self):
        print(f"His name is {self.name} and id is {self.__id}")
        self.__id2()





Sivan=Student("Sivan","43")

Sivan.details()