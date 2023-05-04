def first_non_repeating(str_r):
    dict = {}
    size = len(str_r)
    for i in range(size):
        key = str_r[i]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] = dict[key]+1
    # print(dict)
    for key, value in dict.items():
        if value == 1:
            print(key, value)
            break


first_non_repeating("WAKANDAKN")
