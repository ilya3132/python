parent = 0
for item in range(1,3):
    family_name = input()
    children_family = int(input())
    if children_family > 3:
        print("DISCOUNT")
    parent += children_family
print(parent)