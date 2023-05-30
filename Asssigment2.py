import sys

l = []

def terminationcondition():
    print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
    ask = int(input())
    if ask == 2:
        print("Thank you!")
        sys.exit()


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
    terminationcondition()


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
    terminationcondition()


def pops(container,position,p):
    if len(l) == 0:
        print(container+" is already Empty")

    else:
        print("Value is popped from the "+position)
        print("Updated "+container+" is:")
        l.pop(p)
        print(l)
    terminationcondition()


def sizes(container):
    print("The size of the "+container+" is " + str(len(l)))
    terminationcondition()


def prints(container):
    print("The "+container+" is")
    print(l)
    terminationcondition()


def clears(container):
    l.clear()
    print(container+" is empty now!")
    print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
    terminationcondition()


print("Hello There! What do you want to Implement?")
print("1.Queue 2.Stack")
choice = int(input())


while True:
    if choice == 1:
        choices("QUEUE")
        subchoice = int(input())

        if subchoice == 1:
            pushs("QUEUE")

        elif subchoice == 2:
            pops("QUEUE","FIRST",0)

        elif subchoice == 3:
            inserts("QUEUE")

        elif subchoice == 4:
            sizes("QUEUE")

        elif subchoice == 5:
            prints("QUEUE")

        elif subchoice == 6:
            clears("QUEUE")

        else:
            break

    else:
        choices("STACK")
        subchoice = int(input())

        if subchoice == 1:
            pushs("STACK")
        elif subchoice == 2:
            pops("STACK","LAST",len(l)-1)
        elif subchoice == 3:
            inserts("STACK")
        elif subchoice == 4:
            sizes("STACK")
        elif subchoice == 5:
            prints("STACK")
        elif subchoice == 6:
            clears("STACK")
        else:
            break

print("Thank You!")
