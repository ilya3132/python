def square_digits(num):
    num1 = str(num)
    num2 = ""
    for item in num1:
        item1 = int(item)
        item2 = item1 ** 2
        num2 += str(item2)
        num3 = int(num2)
    return num3
