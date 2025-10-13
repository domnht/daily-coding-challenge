from module_test import do_test

def send_message(route: list) -> float:
    num_of_salleties = len(route) - 1
    total_distance = 0
    for i in range(0, len(route)):
        total_distance += route[i]

    return round(total_distance/300000 + 0.5*num_of_salleties, 4)

do_test(function_name="send_message", should_return=2.5, route=[300000, 300000])
do_test(function_name="send_message", should_return=3.0627, route=[384400, 384400])
do_test(function_name="send_message", should_return=364.5, route=[54600000, 54600000])
do_test(function_name="send_message", should_return=1674.3333, route=[1000000, 500000000, 1000000])
do_test(function_name="send_message", should_return=2.4086, route=[10000, 21339, 50000, 31243, 10000])
do_test(function_name="send_message", should_return=21.1597, route=[802101, 725994, 112808, 3625770, 481239])
