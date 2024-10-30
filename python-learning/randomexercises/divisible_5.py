def disible_by_5(list_num):
    print("Given list:", list_num)
    for num in list_num:
        if num % 5 == 0:
            print("DIvisible by 5:", num)
given_list = [10,20,33,46,55]
disible_by_5(given_list)