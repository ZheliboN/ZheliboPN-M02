#Задача "Все ли равны?":
#На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
first = int(input('Введите целое число №1: '))
second = int(input('Введите целое число №2: '))
third = int(input('Введите целое число №3: '))
#Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.
#Пункты задачи:
#Если все числа равны между собой, то вывести 3
#Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
#Если равных чисел среди 3-х вообще нет, то вывести 0
if first==second and first==third and second==third:
    print(f'Между собой равны 3 числа: first = {first}, second = {second}, third = {third}')
elif first==second or second==third or first==third:
    print('Между собой равны 2 числа:')
    if first==second:
        print(f'first = {first}, second = {second}')
    if second==third:
        print(f'second = {second}, third = {third}')
    if first==third:
        print(f'first = {first}, third = {third}')
else:
    print(f'Среди введенных чисел first = {first}, second = {second}, third = {third} равны между собой 0')
