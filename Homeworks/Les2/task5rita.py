"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
"""

rating = [8, 6, 5, 5, 2, 2]

print(f'Исходный набор чисел: {rating}')

while True:
    user_number = input('Введите новый элемет рейтинга: ')
    if user_number.lower() == 'q':
        break;
    elif user_number.isdigit():
      user_number = int(user_number)
      count = rating.count(user_number)
      position = rating.index(user_number) if user_number in rating else 0
      if user_number in rating:
          rating.insert(position+count, user_number)
      else:
          rating.append(user_number)
          rating.sort(reverse = True)
      print(f'Результат: {rating}')
    else:
          print('Ошибка ввода!')