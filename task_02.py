def coincidence(subsequence,range_list):
    final_list = []
    if len(subsequence) == 0 or len(range_list) < 2:
        return final_list

    for i in subsequence:
        if not isinstance(i, (int, float)):
            continue
        elif (range_list[0] <= i) and (i <= range_list[1]):
            final_list.append(i)
    return final_list

started_list = [None, 1, 'foo', 4, 2, 2.5]
range_list = [1,4]
x = coincidence(started_list, range_list)
print(x)