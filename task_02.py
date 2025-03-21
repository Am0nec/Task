def coincidence(subsequence = None, range_list = None):
    final_list = []

    if subsequence is None or range_list is None:
        return final_list

    if len(subsequence) == 0 or len(range_list) < 2:
        return final_list

    range_start = range_list[0]
    range_end = range_list[-1] - 1

    for i in subsequence:
        if not isinstance(i, (int, float)):
            continue
        elif range_start <= i <= range_end:
            final_list.append(i)
    return final_list

started_list = [None, 1, 'foo', 4, 2, 2.5]
range_list = (1, 4)
x = coincidence(started_list, range_list)
print(x)

