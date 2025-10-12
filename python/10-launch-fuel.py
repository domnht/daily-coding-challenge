from module_test import *

def launch_fuel(payload: int) -> float:
    total_fuel = 0
    current_added_fuel = -1 # Use -1 as initial value

    while current_added_fuel >= 1 or current_added_fuel == -1:
        # Calculate the added fuel after adding fuel mass into total payload mass
        current_added_fuel = (payload + total_fuel) / 5 - total_fuel
        total_fuel += current_added_fuel

    return round(total_fuel, 1)

do_test(function_name="launch_fuel", should_return=12.4, payload=50)
do_test(function_name="launch_fuel", should_return=124.8, payload=500)
do_test(function_name="launch_fuel", should_return=60.7, payload=243)
do_test(function_name="launch_fuel", should_return=2749.8, payload=11000)
do_test(function_name="launch_fuel", should_return=1553.4, payload=6214)
