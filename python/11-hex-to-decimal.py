from module_test import *

def hex_to_decimal(hex: str) -> int:
    hex_chars = list(range(0, 10)) + list(["A", "B", "C", "D", "E", "F"])
    decimal_values = {}
    for i in range(0, 16):
        decimal_values[str(hex_chars[i])] = i

    decimal_result = 0
    num_of_chars = len(hex)
    for char in hex:
        num_of_chars -= 1
        decimal_result += decimal_values[char] * 16 ** num_of_chars
    return decimal_result

do_test(function_name="hex_to_decimal", should_return=10, hex="A")
do_test(function_name="hex_to_decimal", should_return=21, hex="15")
do_test(function_name="hex_to_decimal", should_return=46, hex="2E")
do_test(function_name="hex_to_decimal", should_return=255, hex="FF")
do_test(function_name="hex_to_decimal", should_return=2623, hex="A3F")
