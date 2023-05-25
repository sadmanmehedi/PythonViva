import functools

list=[1,3,5,6,2]

print("The sum of the list element is: ",end="")
print(functools.reduce(lambda a,b:a+b,list))

print("The maximum element of the list is ",end="")
print(functools.reduce(lambda a,b:a if a>b else b,list))