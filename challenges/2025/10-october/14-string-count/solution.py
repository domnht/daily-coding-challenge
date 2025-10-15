from module_test import do_test

def count(text: str, parameter: str) -> int:
    num_of_found = 0
    current_found_position = -1
    for i in range(len(text) - len(parameter) + 1):
        find_result = text.find(parameter, i)
        if find_result >= 0 and find_result != current_found_position:
            num_of_found += 1
            current_found_position = find_result

    return num_of_found

do_test(function_name="count", should_return=2, text="aaa", parameter="aa")
do_test(function_name="count", should_return=1, text="abcdefg", parameter="def")
do_test(function_name="count", should_return=0, text="hello", parameter="world")
do_test(function_name="count", should_return=2, text="mississippi", parameter="iss")
do_test(function_name="count", should_return=3, text="she sells seashells by the seashore", parameter="sh")
do_test(function_name="count", should_return=10, text="101010101010101010101", parameter="101")
