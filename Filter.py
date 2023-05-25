ages=[5,12,34,32,23,54]

def myFunc(x):
    if x<18:
        return False
    else:
        return True

adults=filter(myFunc,ages)

for x in adults:
    print(x)