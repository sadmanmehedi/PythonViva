l=[22,"abc",23.5]

x=list(map(lambda x:x+2 if type(x) is int else x,l))

print(x)
