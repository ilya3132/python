for item in range(1,4790):
    name = input()
    bottle_order = int(input())
    botlle_box = 35
    delivery = 0
    if bottle_order < 4:
        delivery = 10
    print(f'{name} your price {bottle_order * botlle_box + delivery}')

    

