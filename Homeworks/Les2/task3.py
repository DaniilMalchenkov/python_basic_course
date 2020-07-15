"""Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

while True:
    month = input('Введите номер месяца в виде целого числа от 1 до 12: ')
    if month.isdigit():
        month = int(month)
        if month <= 12 and month != 0:
            break
    print('Ошибка ввода.')

# Решение через list
month_list = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f'{month}-й месяц - это {month_list[month - 1]}')

# Решение через dict
month_dict = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима'
}
print(f'{month}-й месяц - это {month_dict.get(month)}')