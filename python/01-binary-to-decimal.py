from module_test import *

def to_decimal(binary: str) -> int:
    decimal_result = 0
    num_of_chars = len(binary)
    for char in binary:
        num_of_chars -= 1
        decimal_result += int(char) * 2 ** num_of_chars
    return decimal_result

do_test(function_name="to_decimal", should_return=5, binary="101",)
do_test(function_name="to_decimal", should_return=10, binary="1010",)
do_test(function_name="to_decimal", should_return=18, binary="10010",)
do_test(function_name="to_decimal", should_return=85, binary="1010101",)
