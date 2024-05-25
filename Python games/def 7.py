age = int(input())
tickets = int(input())
priece = 40
priece2 = 60
if age <= 18:
    print("YOUNG")
    print(tickets * priece)
else:
    print("OLD")
    print(priece2 * tickets)

