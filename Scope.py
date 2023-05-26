#Global Function

def sivan():
    x=17
    print(x)

sivan()


#If i call a function inside from a function
def sivan2():
    x=17
    print(x)
    def sivan3():
        print(x)
    sivan3()

sivan()



#Global Variable
y=200

def Check():
    print(y)

Check()
print(y)


#If we make two variables with the same name inside and outside of a function then it will treat them both as two
# different variables


z=300

def myfunc():
    z=200
    print(z)

myfunc()

print(z)

#Creating global variable inside a function
def globalf():
    global u
    u=33

globalf()
print(u)