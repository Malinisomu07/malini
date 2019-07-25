def malu():
    n=int(input("enter the value"))
    count=0
    while(n>0):
        n=n//10
        count=count+1
        print("the count of natural number is:",count)
malu()
