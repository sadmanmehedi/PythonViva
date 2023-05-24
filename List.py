#How to declare a list
interns=["Sivan","Poushi","Samin","Talimul"]

print(interns)

#List can allow Duplicate Values too
internsduplicate=["Sivan","Sivan","Poushi","Samin","Talimul"]

print(internsduplicate)

#With List I can find the length too
print(len(interns))
print(len(internsduplicate))

#I can take multiple types of data here
list1=["sivan","shammo","mouli"]
list2=[22,324,523,325,523]
list3=[True,False,False,True]

print(list1)
print(list2)
print(list3)

# A list can have multiple types of data types too
Multiple=["Sivan",1999,True]
print(Multiple)

#The Type
print(type(Multiple))

#Assigning with Constructor
sivan=list((22,33,44))

print(sivan)

#Accesing Items
normal=["VivaSoft","Optimizely","RedDot","Samsung"]
print(normal[0])
print(normal[-1])
print(normal[-2])
print(normal[0:2])
print(normal[:1])
print(normal[0:])


#Modifying Value
modification=["Chelsea","Arsenal","Spurs","Fulham"]
print(modification)
modification[3]="Brentford"
print(modification)

#We Can Modify a range of values too
modification[1:3]=["Crystal Palace","Nottingham Forrest"]
print(modification)
modification[1:2]=["Manchester City","Manchester United"]
print(modification)

#Insert Value
modification.insert(0,"Liverpool")
print(modification)