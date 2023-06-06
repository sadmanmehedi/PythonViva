class Dad:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Son(Dad):
    def something(self):
        print(f"Hey this is {self.name}  and my age is {self.age}")

Raju=Dad("Shafiqul Islam Raju",60)
Sivan=Son("Sadman Mehedi Sivan",23)
Sivan.something()