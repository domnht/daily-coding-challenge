from module_test import *
from datetime import date

def moon_phase(date_string):
    # Get year, month, day from given string
    yyyy = int("".join(date_string[0:4]))
    mm = int("".join(date_string[5:7]))
    dd = int("".join(date_string[8:10]))

    # Init date value and reference date
    date_value = date(yyyy, mm, dd)
    reference_date = date(2000, 1, 6)

    # Calculate the difference between input date and reference date
    difference = date_value - reference_date

    # Determine the day is in which day of cycle
    num_of_date_in_cycle = 28
    days = (difference.days + 1) % num_of_date_in_cycle
    days = days if days != 0 else num_of_date_in_cycle

    # Return result
    if days <= 7: return "New"
    if days <= 14: return "Waxing"
    if days <= 21: return "Full"
    return "Waning"

do_test(function_name="moon_phase", should_return="New", date_string="2000-01-12")
do_test(function_name="moon_phase", should_return="Waxing", date_string="2000-01-13")
do_test(function_name="moon_phase", should_return="Full", date_string="2014-10-15")
do_test(function_name="moon_phase", should_return="Waning", date_string="2012-10-21")
do_test(function_name="moon_phase", should_return="New", date_string="2022-12-14")
