print("Hello There! What do you want to Implement?")
print("1.Queue 2.Stack")
print("\n")
choice=int(input())
print(choice)

l=[]

while True :
  if choice==1:
    print("Which Queue operation you want to perform")
    print("1.Push\n2.Pop\n3.Insert\n4.Size\n5.Print\n6.Clear\n7.Exit")
    subchoice=int(input());
    if subchoice==1:
        print("Which Value you want to push?")
        value=int(input())
        l.append(value)
        print("Operation Done!")
        print("Updated Queue is:")
        print(l)

    elif subchoice==2:
        if len(l)==0:
           print("Queue is already Empty")
        else:
            print("Value is popped from the first")
            print("Updated Queue is:")
            l.pop(0)
            print(l)
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
    elif subchoice==4:
        print("The size of the Queue is "+ str(len(l)))
    elif subchoice==5:
        print("The Queue is")
        print(l)
    elif subchoice==6:
        l.clear()
        print("Queue is empty now!")
    else:
        break

  else:
    print("Which Stack operation you want to perform")
    print("1.Push\n2.Pop\n3.Insert\n4.Size\n5.Print\n6.Clear\n7.Exit")
    subchoice=int(input());
    if subchoice==1:
        print("Which Value you want to push?")
        value=int(input())
        l.append(value)
        print("Updated Stack is:")
        print(l)
    elif subchoice==2:
        if len(l)==0:
           print("Stack is already Empty")
        else:
            print("Value is popped from the last")
            print("Updated Stack is:")
            l.pop(0)
            print(l)

    elif subchoice == 3:
        print("Tell me the index and the value you want to insert\n")
        print("Index?\n")
        index = int(input())
        print("Value?\n")
        value = int(input())
        l.insert(index, value)
        print("Updated Stack is:")
        print(l)
    elif subchoice == 4:
        print("The size of the Stack is " + str(len(l)))
    elif subchoice == 5:
        print("The Stack is")
        print(l)
    elif subchoice == 6:
        l.clear()
        print("Stack is empty now!")
    else:
        break



print("Thank You!")


