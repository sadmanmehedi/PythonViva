import os

f = open("demofile.txt","rt")

#print(f.read())


print(f.read(30))
print(f.readline())
print(f.readline())


f.close()

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile.txt", "r")
print(f.read())

os.remove("demofile.txt")

if os.path.exists("demofile3.txt"):
    os.remove("demofile3.txt")
else:
    print("The FIle doesnot exist")