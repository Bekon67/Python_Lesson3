#  Последовательности помещаются во вложенный список. Сортировка не делалась

list_element = []
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
    list_element.append(in_list_element)
for volume in set(list_element[0]):
    if volume in list_element[1]:
        while volume in list_element[0]:
            list_element[0].remove(volume)
print('Результат:', end=' ')
print(*list_element[0], sep=',')
