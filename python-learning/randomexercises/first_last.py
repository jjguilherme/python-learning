def first_last_same(numberList):
    print("Given list:", numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False
    
numbers_x = [10,20,30,40,50,10]
print("result is", first_last_same(numbers_x))

numbers_y = [15,25,35,45,55,65]
print("result is", first_last_same(numbers_y))
