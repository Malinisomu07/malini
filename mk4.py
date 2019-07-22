def mn():
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    c=int(input("enter the value"))
    if(a>b or a>c):
        print("a is GREATEST")
    elif(b>a or b>c):
        print("b is GREATER")
    elif(c>a or c>b):
        print("c is GREATER")
    else:
        print("NOT A GREATEST")
mn()
