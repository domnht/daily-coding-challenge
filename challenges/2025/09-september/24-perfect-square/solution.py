from module_test import do_test
from math import sqrt

def is_perfect_square(n):
    if n < 0: return False
    square_root_of_n = sqrt(n)
    return int(square_root_of_n) == square_root_of_n

do_test(function_name="is_perfect_square", should_return=True, n=9)
do_test(function_name="is_perfect_square", should_return=True, n=49)
do_test(function_name="is_perfect_square", should_return=True, n=1)
do_test(function_name="is_perfect_square", should_return=False, n=2)
do_test(function_name="is_perfect_square", should_return=False, n=99)
do_test(function_name="is_perfect_square", should_return=False, n=-9)
do_test(function_name="is_perfect_square", should_return=True, n=0)
do_test(function_name="is_perfect_square", should_return=True, n=25281)
