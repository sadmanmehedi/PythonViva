print("Hello There! What do you want to Implement?")
print("1.Queue 2.Stack")
print("\n")
choice=int(input())
print(choice)

l=[]
print(type(l))

if choice==1:
    print("So you want to perform Queue")
    print("Which Queue operation you want to perform")
    print("1.Push\n2.Pop\n3.Insert\n4.Size\n5.Print")
    subchoice=int(input());
    if subchoice==1:
        print("Which Value you want to push?")
        value=int(input())
    elif subchoice==2:
        print("Value is popping from the first")
    elif subchoice == 3:
        print("Tell me the index and the value you want to insert\n")
        print("Index?\n")
        index=int(input())
        print("Value?\n")
        value = int(input())
    elif subchoice==4:
        print("The size of the Queue is "+ str(len(l)))
    else:
        print("The Queue is")
        print(l)

else:
    print("So you want to perform Stack")
    print("Which Stack operation you want to perform")
    print("1.Push\n2.Pop\n3.Insert\n4.Size\n5.Print")
    subchoice=int(input());
    if subchoice==1:
        print("Which Value you want to push?")
        value=int(input())
    elif subchoice==2:
        print("Value is popped from the last")
    elif subchoice == 3:
        print("Tell me the index and the value you want to insert\n")
        print("Index?\n")
        index = int(input())
        print("Value?\n")
        value = int(input())
    elif subchoice == 4:
        print("The size of the Stack is " + str(len(l)))
    else:
        print("The Stack is")
        print(l)





