import time
from random import randint as random_between

arrays_for_tests_of_correct = [
    [1, 2, 3],
    [2, 1, 3],
    [44, 2, 44, 9, 0, 0, 13332],
    [i*random_between(-99, 99) for i in range(10)],
    [-1, -2, -3],
    [-2, -2, 1, 1, 0, 100, 2, 300],
    [-0.2, 1, -0.3, 4, 9.9, 44, 0, 0],
]

# отсортировываем наши массивы встроенной питоновской сортировкой для тестирования
sorted_arrays_for_tests_of_correct = list(map(lambda array: sorted(array), arrays_for_tests_of_correct))

def testing_correct_sorts(*funcs_sorts):
    for func in funcs_sorts:
        print("Тестируем корректность: '{doc}'".format(doc=func.__doc__.split('\n')[0]))
        for i, array in enumerate(arrays_for_tests_of_correct):
            array_copy_str = ', '.join(map(str, array.copy()))

            sorted_array = sorted_arrays_for_tests_of_correct[i]
            try:
                sorted_array_by_func = func(array.copy()) # отдаем копию, иначе отсортирует исходный массив

                sorted_array_by_func_str = ', '.join(map(str, sorted_array_by_func))

                if sorted_array != sorted_array_by_func:
                    print("FAIL: [{array_copy_str}] -> [{sorted_array_by_func_str}]".format(
                        array_copy_str=array_copy_str, sorted_array_by_func_str=sorted_array_by_func_str)
                    )
                else:
                    print("OK: [{array_copy_str}] -> [{sorted_array_by_func_str}]".format(
                        array_copy_str=array_copy_str, sorted_array_by_func_str=sorted_array_by_func_str)
                    )
            except Exception as e:
                print("ERROR: [{array_copy_str}] -> {message}".format(array_copy_str=array_copy_str, message=e))

        print()


large_array = list(i*random_between(-99, 99) for i in range(10000, -10000, -1))
large_array_with_repeats_elems = list(random_between(-5, 5) for _ in range(10000, -10000, -1))
array_with_big_range = [2000000000, 1, -20000000]
large_sorted_array = list(i for i in range(-10000, 10000))


def testing_speed_sorts(*funcs_sorts):
    def _print_time(func, array, message):
        start_time = time.time()
        try:
            func(array.copy())
            print("{message}: {time} секунд ".format(message=message, time=round(time.time() - start_time, 2)))
        except Exception as e:
            print("{message}: ERROR - {error}".format(message=message, error=e))

    for func in funcs_sorts:
        print("Тестируем скорость выполнения: '{doc}'".format(doc=func.__doc__.split('\n')[0]))

        _print_time(func, large_array, "Обычный массив")
        _print_time(func, large_array_with_repeats_elems, "Массив с повторяющимися элементами")
        _print_time(func, array_with_big_range, "Массив с большим диапазоном между мин. и макс. элементами")
        _print_time(func, large_sorted_array, "Уже отсортированный массив")

        print()

if __name__ == '__main__':
    from sorts.funcs_sorting_methods import insert_sort, choice_sort, bubble_sort, count_sort, quick_sort
    testing_correct_sorts(insert_sort, choice_sort, bubble_sort, count_sort, quick_sort)
    testing_speed_sorts(insert_sort, choice_sort, bubble_sort, count_sort, quick_sort)
