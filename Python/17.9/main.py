def sort_arr(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


enter_data=input("Введите числовую последовательность:").split()
enter_element=int(input("Введите число для анализа:"))

enter_data=list(map(int,enter_data))
enter_data=sort_arr(enter_data)
print("Список:",enter_data)

if enter_element>enter_data[len(enter_data)-1]:
        print("Число вне диапозона. Попробуйте другое число для анализа.")
        exit()

position=binary_search(enter_data,enter_element,0,len(enter_data))

if position==0:
    if enter_element==enter_data[0]:
        print("Меньше элементов нет. Попробуйте другое число для анализа.")
        exit()
    else:
        print("Такую ошибку никто не ждал. Напишите разработчику.")
        exit()
else:
    print("Подходящее число из списка:",enter_data[position-1])