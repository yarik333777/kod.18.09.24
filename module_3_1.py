calls = 0
def count_calls():
     global calls
     calls+= 1
print(calls)

def string_info(string):
    count_calls()
    my_list = input()
    my_count = len(my_list)
    my_upper = my_list.upper()
    my_lower = my_list.lower()
    print(string)
    return my_list, my_lower, my_upper, my_count
writton = string_info('Введенное число или слова:')
print(writton)

def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(calls)
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True,
# если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).

# Пространства имен (namespaces)
# глобальное (global)
# лкальное (locals)
# обемльюшее (enclosing)
# встроеннное (bulitns)
# обдасть видемасити (scopes)
