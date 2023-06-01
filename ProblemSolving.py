l=[]

a=int(input())
b=int(input())
c=int(input())
d=int(input())

l.append(a)
l.append(b)
l.append(c)
l.append(d)

l.sort()


x=0
y=l[1]
z=l[1]+l[2]-l[1]
print(str(x)+" "+str(y)+" "+str(z))
