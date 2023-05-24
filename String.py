print("Hello")

a="Hello"
print(a)

a="""gwrgwer
wer
wre
werh
wreg
"""

#printing the whole string
print(a)

#Printing as the first element of array
print(a[0])


for x in a:
    print(x)

print(len(a))

txt="The best things in life are free!"

if "free" in txt:
    print("Yes,free is present")

if not "FREE" in txt:
    print("Yes,FREE is not present")

b="Hello"
print(b[2:5])

b="Hello World"
print(b[:5])


c="Sadman"

print(c[3:])
print(b[-5:-2])


p="viva SOf t"
print(p.upper())
print(p.lower())

print(p.strip())

e="Hello World"
print(e.replace("H","J"))


A="HELLO "
B="WORLD"
C=A+" "+B
print(C)

quantity=3
itemno= 568
price=49.95

myorder="I want {} pieces of item {} for {} dollars"

print(myorder.format(quantity,itemno,price))