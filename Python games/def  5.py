name = input()
wheels = int(input())
if wheels > 4:
    print (name, "HEAVY")
elif wheels == 2:
    print(name, "TWO")
elif wheels < 1:
    print (name, "ERROR")
else:
    print("GOOD DAY")