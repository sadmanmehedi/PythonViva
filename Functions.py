def sivan():
    print("Hello From a Function!")
sivan()

def domywork(fname):
    print(fname+" will join Vivasoft as Intern")

domywork("Sivan")
domywork("Talimul")
domywork("Samin")
domywork("Poushi")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Using * it will take the values as list
def hey_function(*kids):
    print("The youngest child is"+kids[2])


my_function("Emil","Tobias","Linus")

#Using ** it will take the values as dictionary

def my_ffunction(**kid):
    print("His last name is"+kid["lname"])

my_ffunction(fname="Tobias",lname="Refense")

#Default Parameters

def country(name="Bangladesh"):
    print("I am from "+name)

country()
country("India")
country("Indonesia")
country("Italy")
country("Thailand")

def trylist(food):
    for x in food:
        print(x)

fruits=["apple","banana","Cherry"]

trylist(fruits)

#Return Value

def retuuurn(x):
    return 5*x

print(retuuurn(32))
print(retuuurn(22))

#Pass Will Do Nothing

def PASS():
    pass

#Recursion
def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return  result


print("\n\n Recursion example result")
tri_recursion(6)
