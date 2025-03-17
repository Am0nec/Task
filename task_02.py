def coincidence(subsequence, range_list):
    final_list = []

    if subsequence == None or range_list == None:
        return final_list

    if len(subsequence) == 0 or len(range_list) < 2:
        return final_list

    for i in subsequence:
        if not isinstance(i, (int, float)):
            continue
        elif (range_list[0] <= i) and (i <= range_list[1]):
            if i == range_list[1]:
                continue
            final_list.append(i)
    return final_list

started_list = [1, 4]
range_list = None
x = coincidence(started_list, range_list)
print(x)
