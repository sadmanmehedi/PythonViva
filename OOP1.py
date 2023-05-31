class Dog:
    pass

a=Dog()
b=Dog()

if a==b:
    print("True")
else:
    print("False")

print(a)
print(b)

class Cat:
    species="Canis familiaris"

    def __init__(self,name,age):
        self.name=name
        self.age=age

c=Cat("fae","fqaw")

print(c.species)

c.species="UNIMART"

print(c.species)