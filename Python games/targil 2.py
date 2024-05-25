for item in range(1,287):
    name = input()
    work =int(input())
    technick = 0
    if work > 25:
        print(name, "bonus")
    technick += work
print(technick)