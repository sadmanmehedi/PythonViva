def choices(container):
    print("Which "+container+" operation you want to perform")
    print("1.Push\n2.Pop\n3.Insert\n4.Size\n5.Print\n6.Clear\n7.Exit")


def pushs(container):
    print("How Many Values to  Push?")
    howmany = int(input())
    print("Okay Input the Values")
    check = 0
    while check < howmany:
        value = int(input())
        l.append(value)
        check = check + 1

    print("Got the value")
    print("Updated" + container + " is: ")
    print(l)
    print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
    ask = int(input())
    if ask == 2:
        print("Thank you!")
        sys.exit()


def inserts(container):
    print("Tell me the index and the value you want to insert\n")
    print("Index?\n")
    index = int(input())
    print("Value?\n")
    value = int(input())
    l.insert(index, value)
    print("Operation Done")
    print("Updated "+container+" is:")
    print(l)
    print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
    ask = int(input())
    if ask == 2:
        print("Thank you!")
        sys.exit()


def pops(container,position,p):
    if len(l) == 0:
        print(container+" is already Empty")

    else:
        print("Value is popped from the "+position)
        print("Updated "+container+" is:")
        l.pop(p)
        print(l)
    print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
    ask = int(input())
    if ask == 2:
        print("Thank you!")
        sys.exit()


def sizes(container):
    print("The size of the "+container+" is " + str(len(l)))
    print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
    ask = int(input())
    if ask == 2:
        print("Thank you!")
        sys.exit()


def prints(container):
    print("The "+container+" is")
    print(l)
    print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
    ask = int(input())
    if ask == 2:
        print("Thank you!")
        sys.exit()


def clears(container):
    l.clear()
    print(container+" is empty now!")
    print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
    ask = int(input())
    if ask == 2:
        print("Thank you!")
        sys.exit()
