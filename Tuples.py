#Basic Tuple
FirstTuple=("London","Manchester","Mersyside")
print(FirstTuple)

#Type of a typle
print(type(FirstTuple))

#A tuple with multiple types of values
SecondTuple=("Sivan",23,True,"Software Engineer")
print(SecondTuple)

ThirdTuple=tuple(("Cha","Coffee","Whipping Cream"))
print(ThirdTuple)


#Accesing Tuple Can be done With Index Values
ForthTuple=(21321,4123,124,134)
print(ForthTuple[2])
print(ForthTuple[-1])

#ByRanging is also Possible
print(ForthTuple[1:])

#Tuple is unchangeable so we cannot change the values once initiated
SixTuple=(1,2,3,4,5)
#SixTuple[0]=18
print(SixTuple)


#But there is this Unpacking a Tuple Which is pretty Nice!
fruits=("crimson cup","secret recipe","sao 26")
(a,b,c)=fruits
print(a)
print(b)
print(c)

#Also joining tuple is possible
IUT=("SWE","CSE","CEE","TVE","BTM")
BUET=IUT*2
print(BUET)