houseAddress= {
    "Place":"Nikunja 2",
    "House":"37",
    "Road":"29"
}

print(houseAddress["House"])
print(houseAddress)


print(len(houseAddress))

#Multiple Type Variables
monthBill={
    "Electricity":True,
    "HowMuch":2352
}

print(monthBill["HowMuch"])

print(type(monthBill))

x=monthBill.get("HowMuch")
print(x)

print(monthBill.keys())


#New Key Value has been added
monthBill["Internet"]=500

print(monthBill)

#Value can be modified too
monthBill["Internet"]=42100

print(monthBill)

#Adding Item with update keyword
monthBill.update({"servicecharge":4500})

print(monthBill)

#For Removing Item we can use this pop thing
monthBill.pop("Internet")
print(monthBill)

del monthBill["servicecharge"]
print(monthBill)


#Making the list empty
#monthBill.clear()
print(monthBill)

#Copying the dictionary
newBill=monthBill.copy()

print(newBill)


#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child3"]["year"])