tickets = 48
people = int(input())
if people > 100:
    tickets = 43
    print(tickets * people)
else:
    print(tickets * people)