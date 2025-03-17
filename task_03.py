def max_odd(array):
    y = 0
    j = 0
    if len(array) == 0:
        return None
    for i in array:
        if not isinstance(i, (int, float)):
            continue
        if i % 2 == 0 :
            continue
        elif i >= y:
            y = i
            j += 1
    if j == 0:
        return None
    return y

started_list = [2,2,4]
x = max_odd(started_list)
print(x)
