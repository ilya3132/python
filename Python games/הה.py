num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1 == num2 or num1 == num3:
    print("erer")
elif num2 == num3 or num2 == num1:
    print("erer")
elif num3 == num2 or num3 == num1:
    print("erer")
else:
    print((num1 + num2 + num3) / 3)