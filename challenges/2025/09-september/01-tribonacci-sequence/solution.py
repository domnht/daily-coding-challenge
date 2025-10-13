from module_test import do_test

def tribonacci_sequence(start_sequence, length):

    return length

do_test(function_name="tribonacci_sequence", should_return=[0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513], start_sequence=[0, 0, 1], length=20)
do_test(function_name="tribonacci_sequence", should_return=[21], start_sequence=[21, 32, 43], length=1)
do_test(function_name="tribonacci_sequence", should_return=[], start_sequence=[0, 0, 1], length=0)
do_test(function_name="tribonacci_sequence", should_return=[10, 20], start_sequence=[10, 20, 30], length=2)
do_test(function_name="tribonacci_sequence", should_return=[10, 20, 30], start_sequence=[10, 20, 30], length=3)
do_test(function_name="tribonacci_sequence", should_return=[123, 456, 789, 1368, 2613, 4770, 8751, 16134], start_sequence=[123, 456, 789], length=8)
