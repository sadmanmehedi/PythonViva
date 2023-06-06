from abc import ABC,abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self,arg):
        pass

class MyClass(MyInterface):
    def method1(self):
        print("Implementing Method1")

    def method2(self,arg):
        print(f"Implementing method2 with argument:{arg}")


obj=MyClass()
obj.method1()
obj.method2("Hello World")
