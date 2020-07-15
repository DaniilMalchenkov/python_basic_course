"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()."""

i = 0
user_list = []

while True:
    len_list = input('Укажите длину списка: ') # Запрашиваем длину списка
    if len_list.isdigit():
        len_list = int(len_list)
        break
    print('Ошибка ввода. Необходимо ввести число!')

while i < len_list:
    user_list.append(input(f'Введите элемент №{i+1}: ')) # Запрашиваем каждый элемент
    i += 1

k = 0
if len_list % 2 == 0: # Проверяем длину на четность
    while k < len_list:
        user_list.insert(k, user_list[k+1])
        user_list.pop(k+2)
        k += 2
else:
    while (k < len_list - 1):
        user_list.insert(k, user_list[k+1]) # Не включаем последний элемент
        user_list.pop(k+2)
        k += 2

print(user_list)