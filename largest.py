def malu():
    a=int(input("enter the value"))
    b=int(input("enter the value"))
    c=int(input("enter the value"))
    if((a>b) and (a>c)):
        largest=a
    elif((b>a) and (b>c)):
        larges=b
    else:
        largest=c
    print("The largest is",largest)
malu()
