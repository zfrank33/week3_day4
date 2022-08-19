def zeros_move(arr_num):
    zero_store = list()
    real_store = list()
    # print("len(arr_num)")
    # print(arr_num[7])
    # print(len(arr_num))
    count = 0
    # for a in arr_num:
    for i in range(len(arr_num)):
        a = arr_num[i]
        count = count+1
        # print("count ------------>>>>>>"+str(count))
        # print("i ------------>>>>>>"+str(i))

        # print("a == "+str(a))
        if a == 0:
            zero_store.append(0)
        if a !=0:
            real_store.append(a)
            # arr_num.remove(0)
    # print("arr_num")
    # print(arr_num)
    # print("zero_store")
    # print(zero_store)
    # print("real_store")
    # print(real_store)
    # print(real_store+zero_store)
    return real_store+zero_store
# zeros_move([0, 1, 0, 3, 12])
# zeros_move( [1, 7, 0, 0, 8, 0, 10, 12, 0, 4])

        