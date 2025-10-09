from module_test import *

def to_binary(decimal: int):
    binary_result = ""
    current_quotient = decimal
    while current_quotient != 0:
        current_remainder = current_quotient % 2
        current_quotient = int(current_quotient / 2)
        binary_result = str(current_remainder) + binary_result
    return binary_result

do_test(function_name="to_binary", should_return="101", decimal=5)
do_test(function_name="to_binary", should_return="1100", decimal=12)
do_test(function_name="to_binary", should_return="110010", decimal=50)
do_test(function_name="to_binary", should_return="1100011", decimal=99)
