teoria = int(input("how much you get on the teoria test??? "))
age = int(input("how old are you?????"))
drive = int(input("how much did you got on drive test???? "))
if teoria >56 and age > 17 and teoria > 56:
    print("you can have the driving liscence")
elif teoria < 56 and age > 17 and teoria > 56:
    print("you cant have the liscence bc you got",teoria,"on the teoria test")
elif teoria < 56 and age < 17 and teoria > 56:
    print("you can have the liscence bc yore age is ",age)
elif teoria < 56 and age > 17 and teoria < 56:
    print("you cant have the liscence bc you got",drive,"on the drive test")
else:
    print("you have to study more")