for day in range(31):
    temp = int(input())
    if temp < 10:
        print(" very cold")
    elif 10 < temp < 17:
        print("cold")
    elif 18 < temp < 22:
        print("normal")
    elif 22 < temp < 30:
        print("hot")
    else:
        print("very hot")