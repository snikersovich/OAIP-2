#Задача 1
print('НЕТ') if input() != 'Python' else print('ДА')

#Задача 2
a, b = input(), input()
if a and b == 'да' or a and b == 'нет':
    print('ВЕРНО')
else:
    print('НЕВЕРНО')

#Задача 3
a, b, c = input(), input(), input()
if f'{a}{b}{c}' == '123' or f'{a}{b}{c}' == 'раздватри':
    print('ГОРИ')
else:
    print('НЕ ГОРИ')

#Задача 4
t1, t2 = input(), input()
if t1 != t2 and (t1 == 'Тула' and t2 != 'Пенза' or t2 == 'Пенза' and t1 != 'Тула'):
    print('ДА')
else:
    print('НЕТ')

#Задача 5
n, m = int(input()), int(input())
print(n // m + 1 if n % m else n // m)

#Задача 6
w = input()
print('Подходит') if ((int(w[0]) + int(w[2])) % 8 != 0) and w[1] == '3' else print(f'{int(w[0]) + int(w[2])} {w[1]}')

#Задача 7
a = input('Категория:\n')
if a.lower() == 'продукты':
    b = int(input('Цена:\n'))
    if b <= 100:
        print('Попробуйте нашу выпечку!')
    elif 100 < b <= 500:
        print('Как насчет орехов в шоколаде?')
    else:
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома!')

#Задача 8
a = int(input('Цена первого товара:\n'))
b = int(input('Цена второго товара:\n'))
c = int(input('Цена третьего товара:\n'))

if a > b > c:
    print(f'Акция!\nК оплате: {(a + b + c) // 3}')
elif a < b < c:
    print(f'Акция!\nК оплате: {(a + b + c) // 2}')
else:
    print(f'К оплате: {a + b + c}')

#Задача 9
a = int(input('Покупатели за позавчера:\n'))
b = int(input('Покупатели за вчера:\n'))
if a < b:
    print(f'Сегодня магазин посетит: {b + (b - a)} человек')
elif a > b:
    print(f'Сегодня магазин посетит: {b - (a - b)} человек')

#Задача 10
year = int(input())
print('да') if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) else print('нет')

#Задача 11
print('четное') if int(input()) % 2 == 0 else print('нечетное')