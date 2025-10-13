from module_test import do_test

def is_spam(number: str) -> bool:
    # Get A, B, C, D from input string
    number_array = number.split(" ")
    country_code = number_array[0][1:]
    area_code = number_array[1][1:-1]
    local_number_1 = number_array[2][0:3]
    local_number_2 = number_array[2][4:9]

    # Check each criteria
    # Criteria 1
    if len(country_code) > 2 or not country_code.startswith("0"):
        return True

    # Criteria 2
    area_code_value = int(area_code)
    if area_code_value > 900 or area_code_value < 200:
        return True

    # Criteria 3
    local_number_sum = int(local_number_1[0]) + int(local_number_1[1]) + int(local_number_1[2])
    if str(local_number_sum) in local_number_2:
        return True

    # Criteria 4
    last_char = country_code
    num_of_repeat_times = 1
    for char in (country_code + area_code + local_number_1 + local_number_2):
        if last_char == char:
            num_of_repeat_times += 1
        else:
            last_char = char
            num_of_repeat_times = 1
        if num_of_repeat_times >= 4:
            return True
    return False

do_test(function_name="is_spam", should_return=False, number="+0 (200) 234-0182")
do_test(function_name="is_spam", should_return=True, number="+091 (555) 309-1922")
do_test(function_name="is_spam", should_return=True, number="+1 (555) 435-4792")
do_test(function_name="is_spam", should_return=True, number="+0 (955) 234-4364")
do_test(function_name="is_spam", should_return=True, number="+0 (155) 131-6943")
do_test(function_name="is_spam", should_return=True, number="+0 (555) 135-0192")
do_test(function_name="is_spam", should_return=True, number="+0 (555) 564-1987")
do_test(function_name="is_spam", should_return=False, number="+00 (555) 234-0182")
