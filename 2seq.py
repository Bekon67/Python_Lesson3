# Сделана проверка на ввод: неверного разделителя, двойного разделителя, разных разделителей
# отсутствие разделителя (длинное число)
# двойной цифры


separator = {',', ';', '/'}
get_str = ''
flag = False
while flag is False:
    get_str = input(f'Введите любые цифры через любой из разделителей (запятую, точку с запятой, слэш).\n'
                    f'Разделитель можно использовать  только одного типа: ')
    digit_list = []
    no_digit_list = []
    p_flag_digit = False
    flag_double_symbol = True
    flag_separator = False
    for character in get_str:
        flag_digit = character.isdigit()
        if flag_digit is True:
            if flag_digit == p_flag_digit:
                flag_double_symbol = False
                print('Вы ввели более одной цифры подряд!\n')
            else:
                digit_list.append(character)
        else:
            if flag_digit == p_flag_digit:
                flag_double_symbol = False
                print('Вы ввели двойной разделитель!\n')
            else:
                no_digit_list.append(character)
        p_flag_digit = flag_digit

    no_digit_set = set(no_digit_list)
    if not no_digit_set.issubset(separator):
        print('Вы ввели недопустимый разделитель!\n')
    elif len(no_digit_set) == 0:
        print('Вы не ввели разделителей!n')
    elif len(no_digit_set) > 1:
        print('Вы ввели различные разделители!n')
    else:
        flag_separator = True
    flag = flag_double_symbol and flag_separator

for volume in set(digit_list):
    if digit_list.count(volume) > 1:
        while volume in digit_list:
            digit_list.remove(volume)
print('Результат:', end=' ')
print(*digit_list, sep=',')
