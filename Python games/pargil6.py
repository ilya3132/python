doctor = 0
for item in range(1,275):
    name = input()
    year = int(input())
    blood = input()
    if blood == "O":
        doctor += 1
print(doctor)