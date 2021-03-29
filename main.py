num = int(input())
if 1 <= num <= 10:
    if num % 2 != 0:
        print('красный')
    else:
        print('черный')
if 11 <= num <= 18:
    if num % 2 != 0:
        print('черный')
    else:
        print('красный')
if 19 <= num <= 28:
    if num % 2 != 0:
        print('красный')
    else:
        print('черный')
if 29 <= num <= 36:
    if num % 2 != 0:
        print('черный')
    else:
        print('красный')
if num == 0:
    print('зеленый')
if num < 0 or num > 36:
    print('ошибка ввода')