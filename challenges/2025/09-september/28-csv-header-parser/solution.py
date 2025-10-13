from module_test import do_test

def get_headings(csv: str) -> list:
    headings = [heading.strip() for heading in csv.split(",")]
    return headings

do_test(function_name="get_headings", should_return=["name", "age", "city"], csv="name,age,city")
do_test(function_name="get_headings", should_return=["first name", "last name", "phone"], csv="first name,last name,phone")
do_test(function_name="get_headings", should_return=["username", "email", "signup date"], csv="username , email , signup date ")
