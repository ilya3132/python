def is_prime(num)
    """
    
    :param num: -an integer number
    :return: returns if the number is prime or not
    """
    for i in range(2,num//2):
        if num % i == 0:
            return False
        return True
print(  is_prime(35) )
print( is_prime(53) )
print( is_prime(31))
print(is_prime(13))
print(is_prime(13))
print(is_prime(11))
print(is_prime(5))
print(is_prime(3))
print(is_prime(9))
print(is_prime(22))


def sum_of_numbers(lst):
    """

    :param lst: a list of numbers example [12,5,3,7,90,-10]
    :return: the sum of all the numbers in list
    """
    sun = 0
    for item in lst:
        sun+=item
        return sum


    shum = sum_of_numbers([8,6,10,17,5,3])
    print(shum)