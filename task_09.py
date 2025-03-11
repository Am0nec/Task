def connect_dicts(dict1, dict2):
    mas1 = []
    mas2 = []
    sum_value1 = 0
    sum_value2 = 0
    for value in dict1.values():
        sum_value1 += value
    for value in dict2.values():
        sum_value2 += value

    for key in dict1:
        if dict1[key] <= 10:
            mas1.append(key)
    for i in mas1:
        del dict1[i]

    for key in dict2:
        if dict2[key] <= 10:
            mas2.append(key)
    for i in mas2:
        del dict2[i]

    new_dict = 0
    if sum_value1 == sum_value2 or sum_value1 < sum_value2:
        new_dict =  {**dict1, **dict2}
    if sum_value1 > sum_value2:
            new_dict = {**dict2, **dict1}

    return new_dict

dict1 = { "a": 14, "b": 12, "c": 15, }
dict2 = { "c": 12, "a": 12, "g": 12,}
x = connect_dicts(dict1,dict2)
print(x)
