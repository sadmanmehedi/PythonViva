#Here we converting from JSON TO PYTHON Dictionary

import json

x='{"name":"Sivan","Age":"23","City":"Dhaka"}'

y=json.loads(x)

print(y["City"])

#Here we are doing the opposite by converting from  Dictionary TO JSON

x={

    "name":"Sivan",
    "Age":"23",
     "City":"Dhaka"
}


y=json.dumps(x)

print(y)
