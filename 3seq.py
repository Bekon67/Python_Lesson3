#  Последовательности помещаются во вложенный список. Сортировка не делалась
ext_list_element = []
for k in range(2):
    in_list_element = []
    count_element = ''
    while count_element.isdigit() is False:
        count_element = input(f'Введите количество элементов {k + 1}-го списка: ')
    for i in range(1, int(count_element) + 1):
        get_element = ''
        len_element = 0
        while get_element.isdigit() is False or len_element != 1:
            get_element = input(f'Введите {i}-й элемент из одной цифры: ')
            len_element = len(get_element)
        in_list_element.append(int(get_element))
    #  print(f'Вывод: {in_list_element}')
    in_list_element = set(in_list_element)
    #  print(f'Вывод: {in_list_element}')
    ext_list_element.append(in_list_element)
print('Результат:', end=' ')
print(*(ext_list_element[0] - ext_list_element[1]), sep=',')
