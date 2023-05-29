try:
    print("SIVAN")
except NameError:
    print("Variable X is not defined")
except:
    print("An Exception Occured")
else:
    print("No Errors brother")

try:
    print(x)
except NameError:
    print("Variable X is not defined")
except:
    print("An Exception Occured")
finally:
    print("CHILL brother")

y=-1
if y<0:
    raise Exception("Sorry, No numbers were below 0")

x="Hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")