from module_test import do_test
import time

def speeding(speeds: list, limit: int) -> list:
    speedings = [speed - limit for speed in speeds if speed > limit]
    num_of_speedings = len(speedings)
    if num_of_speedings == 0:
        return [0, 0]
    average_speedings = sum(speedings) / num_of_speedings
    average_speedings = int(average_speedings) if average_speedings == int(average_speedings) else average_speedings
    return [num_of_speedings, average_speedings]

do_test(function_name="speeding", should_return=[0, 0], speeds=[50, 60, 55], limit=60)
do_test(function_name="speeding", should_return=[2, 4], speeds=[58, 50, 60, 55], limit=55)
do_test(function_name="speeding", should_return=[4, 8.5], speeds=[61, 81, 74, 88, 65, 71, 68], limit=70)
do_test(function_name="speeding", should_return=[2, 3.5], speeds=[100, 105, 95, 102], limit=100)
do_test(function_name="speeding", should_return=[1, 57], speeds=[40, 45, 44, 50, 112, 39], limit=55)
