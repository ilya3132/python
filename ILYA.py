from random import randint

a = []
n = int(input())
for i in range(n):

    a.append(randint(0,12393))
print(a)

for i in range(n -1):
    for b in range(n -1 -i):
        if a[b] > a[b+1]:
            a[b],a[b+1] = a[b+1],a[b]
print(a)