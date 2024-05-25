for item in range(0,11):
    num1 = int(input("put here a number "))
    num2 = int(input("put here a number "))
    if num1<num2:
        for i in range(num1,num2+1):
            print(i,end=" ")
    else:
        for i in range(num2,num1+1):
            print(i,end=" ")
    print( )
