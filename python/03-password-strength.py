from module_test import *

def check_strength(password: str):
    has_8_chars = len(password) >= 8
    has_uppercase_letters = False
    has_lowercase_letters = False
    has_number = False
    has_special_chars = False
    for char in password:
        if char.islower() and not has_lowercase_letters: has_lowercase_letters = True
        if char.isupper() and not has_uppercase_letters: has_uppercase_letters = True
        if char.isnumeric() and not has_number: has_number = True
        if char in ["!", "@", "#", "$", "%", "^", "&", "*"] and not has_special_chars: has_special_chars = True

    num_of_rules = int(has_8_chars) + int(has_uppercase_letters and has_lowercase_letters) + int(has_number) + int(has_special_chars)
    print("=> num_of_rules:", num_of_rules)
    if num_of_rules >= 4: return "strong"
    if num_of_rules >= 2: return "medium"
    return "weak"

do_test(function_name="check_strength", should_return="weak", password="123456")
do_test(function_name="check_strength", should_return="weak", password="pass!!!")
do_test(function_name="check_strength", should_return="weak", password="Qwerty")
do_test(function_name="check_strength", should_return="weak", password="PASSWORD")
do_test(function_name="check_strength", should_return="medium", password="PASSWORD!")
do_test(function_name="check_strength", should_return="medium", password="PassWord%^!")
do_test(function_name="check_strength", should_return="medium", password="qwerty12345")
do_test(function_name="check_strength", should_return="medium", password="PASSWORD!")
do_test(function_name="check_strength", should_return="medium", password="PASSWORD!")
do_test(function_name="check_strength", should_return="strong", password="S3cur3P@ssw0rd")
do_test(function_name="check_strength", should_return="strong", password="C0d3&Fun!")
