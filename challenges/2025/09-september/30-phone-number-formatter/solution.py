from module_test import do_test

def format_number(number: str) -> str:
    if len(number) < 11 or not number.isnumeric(): return ""
    return "+{0} ({1}) {2}-{3}".format(
        number[0],
        "".join(number[1:4]),
        "".join(number[4:7]),
        "".join(number[7:11])
    )

do_test(function_name="format_number", should_return="+0 (555) 234-0182", number="05552340182")
do_test(function_name="format_number", should_return="+1 (555) 435-4792", number="15554354792")
