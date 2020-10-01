n=int(input("Enter Number Of Rows = "))
for i in range(n//2,-n//2,-1):
    for j in range(n//2,-1,-1):
        if(j>=abs(i)):
            print("*",end='')
    print()
