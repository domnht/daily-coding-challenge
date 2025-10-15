from module_test import do_test

def is_mirror(str1: str, str2: str) -> bool:
    str1_without_symbol = "".join(char for char in str1 if char.isalpha())
    str2_without_symbol = "".join(char for char in str2 if char.isalpha())
    return str1_without_symbol == str2_without_symbol[::-1]

do_test(function_name="is_mirror", should_return=False, str1="helloworld", str2="helloworld")
do_test(function_name="is_mirror", should_return=True, str1="Hello World", str2="dlroW olleH")
do_test(function_name="is_mirror", should_return=True, str1="RaceCar", str2="raCecaR")
do_test(function_name="is_mirror", should_return=False, str1="RaceCar", str2="RaceCar")
do_test(function_name="is_mirror", should_return=False, str1="Mirror", str2="rorrim")
do_test(function_name="is_mirror", should_return=True, str1="Hello World", str2="dlroW-olleH")
do_test(function_name="is_mirror", should_return=True, str1="Hello World", str2="!dlroW !olleH")
