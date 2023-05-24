x= lambda a:a+10


print(x(5))


def myyfunc(n):
    return lambda a: a*n


 mydoubler= myyfunc(2)

 print(mydoubler(11))