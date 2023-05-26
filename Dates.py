import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.date)


#Using Constructor
y = datetime.datetime(2020, 5, 17)

print(y.strftime("%B"))