class birthday:
    def __init__(self,name,date):
        self.name=name
        self.date=date

    def __stri__(self):
        return f"{self.name} has a birthday on {self.date}"


anam=birthday("Anam","3 June")

print(anam)
print(anam.__stri__())