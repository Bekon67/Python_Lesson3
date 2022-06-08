#  сделал проверку на ввод - одной цифры
list_element = []
count_element = ''
while count_element.isdigit() is False:
    count_element = input('Введите количество элементов: ')
for i in range(1, int(count_element) + 1):
    get_element = ''
    len_element = 0
    while get_element.isdigit() is False or len_element != 1:
        get_element = input(f'Введите {i}-й элемент из одной цифры: ')
        len_element = len(get_element)
    list_element.append(int(get_element))
list_element.sort()
print(f'Вывод: {list_element}')
