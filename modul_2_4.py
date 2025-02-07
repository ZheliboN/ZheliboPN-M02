#Задача "Всё не так уж просто":
#Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Используя этот список составьте второй список primes содержащий только простые числа.
#А так же третий список not_primes, содержащий все не простые числа.
#Выведите списки primes и not_primes на экран(в консоль).
#Пункты задачи:
#Создайте пустые списки primes и not_primes.
primes = []
not_primes = []
#При помощи цикла for переберите список numbers.
for numb in numbers:
    #Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
    #Отметить простоту числа можно переменной is_prime, записав в неё занчение True перед проверкой.
    is_prime = True
    if numb != 1:
        for i in range(2,numb):
            if numb % i == 0:
                is_prime = False
                break
        # В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes в зависимости
        # от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
        if is_prime:
            primes.append(numb)
        else:
            not_primes.append(numb)
#Выведите списки primes и not_primes  на экран(в консоль).
print('Список простых чисел: ', primes)
print('Список не простых чисел: ', not_primes)