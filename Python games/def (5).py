import random
sea = 0
for item in range(1,31):
    coat = ["black","red","white"]
    flug = random.choice(coat)
    print(flug)
    if flug == "black":
        print("you cant enter the sea")
        sea += 1
print(sea)
