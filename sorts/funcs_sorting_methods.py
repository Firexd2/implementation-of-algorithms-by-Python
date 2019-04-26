def insert_sort(array):
    """Сортировка вставками [O(n^2)]"""
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1

    return array


def choice_sort(array):
    """Сортировка методом выбора [O(n^2)]"""
    len_array = len(array)
    for i in range(len_array):
        min = array[i]
        index_min = i
        for j in range(i + 1, len_array):
            if array[j] < min:
                min = array[j]
                index_min = j
        array[i], array[index_min] = array[index_min], array[i]

    return array


def bubble_sort(array):
    """Сортировка методом пузырька [O(n^2)]"""
    len_array = len(array)
    for top_index in range(len_array - 1, 0, -1):
        for i in range(top_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return array


def count_sort(array):
    """Сортировка модифицированным методом подсчета [O(n^2) (при отсортированном массиве, а так n*log n)]
    Минусы:
    - при отсортированном массиве O(n^2)
    - только для целочисленных чисел (можно домодифицировать засчет памяти)
    - при большой разнице между мин. и макс. значением будет выделятся ОЧЕНЬ много памяти
    """
    # находим минимум и максимум в массиве
    min = array[0]
    max = array[0]
    for elem in array[1:]:
        if elem < min: min = elem
        if elem > max: max = elem
    # проинициализируем служебный массив, в котором будут хранится количество определенных элементов в array
    count_elems = [0] * (max - min + 1)
    # т.к. элементы в массиве могут быть меньше или больше 0, фиксируем смещение от 0, которое потом будем
    # компенсировать при подсчете результата
    offset = min
    for elem in array:
        count_elems[elem - offset] += 1

    result = []
    for i, count in enumerate(count_elems):
        for _ in range(count):
            result.append(i + offset)

    return result


def quick_sort(array):
    """Быстрая сортировка, в среднем [O(n*log n)]
    Минусы:
    - не подходит для отсортированного массива
    """
    if not array:
        return array

    support_elem = array[-1]
    array_smaller_elems, array_equal_elems, array_highest_elems = [], [], []

    for elem in array:
        if elem > support_elem:
            array_highest_elems.append(elem)
        elif elem < support_elem:
            array_smaller_elems.append(elem)
        else:
            array_equal_elems.append(elem)

    return quick_sort(array_smaller_elems) + array_equal_elems + quick_sort(array_highest_elems)
