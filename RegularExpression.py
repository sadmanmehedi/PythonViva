import re

txt="The rain in Spain"
x=re.search("^The. *Spain$",txt)

if x:
    print("Yes! We have a match")
else:
    print("We dont have a match")

txt="The rain in Spain"
x=re.findall("ai",txt)
print(x)
txt="The rain in Spain"
x=re.findall("Portugal",txt)
print(x)


txt="The rain in spain"
x=re.search("\s",txt)

print("The first white space character is located in position ",x.start())


txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

txt1="The rain Bangladesh"
y=re.split("\s",txt)
print(y)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


txt="The Rain in Italyta"

x=re.search("ta",txt)

print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
