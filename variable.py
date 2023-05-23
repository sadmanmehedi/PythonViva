#normal assignment and pritning
a=17
name="Sivan"

print(a)
print(name)

#typpecast
x=str(3)
y=int(3)
z=float(3)

#Seeing the types
print(type(x))
print(type(y))
print(type(z))

#Combining and printing
p="Sadman"
q="Mehedi"

print(p+"  "+q)

#Ways to express a variablename
myvar="Anam"
my_var="Anam"
_my_var="Anam"
myVar="Anam"
MYVAR="ANAM"
myvar2="Anam"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#all the assignments in one line
g,h,i="Faisal","Mehedi","Shammo"
print(x)
print(y)
print(z)

#Assigning Multiple Variables with the same value
t=y=u="Chelsea"
print(t)
print(y)
print(z)


#printing in the same line
first="Python"
second="is"
third="Awesome"
print(first,second,third)


#combining number and a string
nm=str(17)
st="Anam"
print(st+nm)


#GlobalVariable
globalvariable="Twenty Two"

def myfunc():
 print("Line number "+globalvariable)

myfunc()

#global in a function

def anotherf():
    global xx
    xx="sad"
    print("SAD"+xx)

anotherf()
