def sort_list(array):
    if len(array) == 0:
        return []

    for i in array:
        if not isinstance(i, int):
            return 'Массив состоит не из целых чисел'

    max_num = max(array)
    min_num = min(array)

    for i in range(len(array)):
        if array[i] == max_num:
            array[i] = min_num
        elif array[i] == min_num:
            array[i] = max_num
    array.append(min_num)
    return array


started_list = [1,2,1,3]
x = sort_list(started_list)
print(x)