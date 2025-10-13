from module_test import do_test

def second_largest(arr):
    larges_1 = arr[0]
    larges_2 = arr[1]
    for number in arr:
        if number < larges_1 and larges_2 == larges_1:
            larges_2 = number
        if number > larges_2:
            if number > larges_1:
                larges_2 = larges_1
                larges_1 = number
            if number < larges_1:
                larges_2 = number
    return larges_2

do_test(function_name="second_largest", should_return=3, arr=[1, 2, 3, 4])
do_test(function_name="second_largest", should_return=94, arr=[20, 139, 94, 67, 31])
do_test(function_name="second_largest", should_return=4, arr=[2, 3, 4, 6, 6])
do_test(function_name="second_largest", should_return=55.5, arr=[10, -17, 55.5, 44, 91, 0])
do_test(function_name="second_largest", should_return=0, arr=[1, 0, -1, 0, 1, 0, -1, 1, 0])
