import sys


print("Hello There! What do you want to Implement?")
print("1.Queue 2.Stack")
print("\n")
choice=int(input())

l=[]

while True :
  if choice==1:
    print("Which Queue operation you want to perform")
    print("1.Push\n2.Pop\n3.Insert\n4.Size\n5.Print\n6.Clear\n7.Exit")
    subchoice=int(input());
    if subchoice==1:
        print("How Many Values to  Push?")
        Howmany=int(input())
        print("Okay Input the Values")
        check=0
        while check<Howmany:
           value=int(input())
           l.append(value)
           check=check+1

        print("Got the value")
        print("Updated Queue is:")
        print(l)
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask=int(input())
        if ask==2:
            print("Thank you!")
            sys.exit()

    elif subchoice == 2:
        if len(l)==0:
           print("Queue is already Empty")

        else:
            print("Value is popped from the first")
            print("Updated Queue is:")
            l.pop(0)
            print(l)
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    elif subchoice == 3:
        print("Tell me the index and the value you want to insert\n")
        print("Index?\n")
        index=int(input())
        print("Value?\n")
        value = int(input())
        l.insert(index, value)
        print("Operation Done")
        print("Updated Queue is:")
        print(l)
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    elif subchoice==4:
        print("The size of the Queue is "+ str(len(l)))
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    elif subchoice==5:
        print("The Queue is")
        print(l)
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    elif subchoice==6:
        l.clear()
        print("Queue is empty now!")
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    else:
        break

  else:
    print("Which Stack operation you want to perform")
    print("1.Push\n2.Pop\n3.Insert\n4.Size\n5.Print\n6.Clear\n7.Exit")
    subchoice=int(input());
    if subchoice == 1:
        print("How Many Values to  Push?")
        Howmany = int(input())
        print("Okay Input the Values")
        check = 0
        while check < Howmany:
            value = int(input())
            l.append(value)
            check = check + 1

        print("Got the value")
        print("Updated Stack is:")
        print(l)
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    elif subchoice==2:
        if len(l)==0:
           print("Stack is already Empty")
        else:
            print("Value is popped from the last")
            print("Updated Stack is:")
            l.pop()
            print(l)
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()

    elif subchoice == 3:
        print("Tell me the index and the value you want to insert\n")
        print("Index?\n")
        index = int(input())
        print("Value?\n")
        value = int(input())
        l.insert(index, value)
        print("Updated Stack is:")
        print(l)
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    elif subchoice == 4:
        print("The size of the Stack is " + str(len(l)))
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    elif subchoice == 5:
        print("The Stack is")
        print(l)
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    elif subchoice == 6:
        l.clear()
        print("Stack is empty now!")
        print("Back to Main Menu?\n1.Yes\n2.No Terminate The Program")
        ask = int(input())
        if ask == 2:
            print("Thank you!")
            sys.exit()
    else:
        break



print("Thank You!")


