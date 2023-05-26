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
    print("1.Push\n2.Pop\n3.Insert\n4.Size")
    subchoice=int(input());
    if subchoice==1:
        print("Which Value you want to push?")
    elif subchoice==2:
        print("Value is popping from the first")
    elif subchoice == 3:
        print("Tell me the index and the value you want to insert\n")
        print("Index?\n")
        index=int(input())
        print("Value?\n")
        value = int(input())
    else
        print("The size of the Queue is" + len(l))

else:
    print("So you want to perform Stack")
    print("Which Stack operation you want to perform")
    print("1.Push\n2.Pop\n3.Insert\n4.Size")
    subchoice=int(input());
    if subchoice==1:
        print("Which Value you want to push?")
    elif subchoice==2:
        print("Value is popped from the last")
    elif subchoice == 3:
        print("Tell me the index and the value you want to insert\n")
        print("Index?\n")
        index = int(input())
        print("Value?\n")
        value = int(input())
    else
        print("The size of the Stack is"+len(l))




