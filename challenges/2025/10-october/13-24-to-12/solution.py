from module_test import do_test

def to_12(time: str) -> str:
    HH = time[0] + time[1]
    MM = time[2] + time[3]
    HH_value = int(HH)
    if HH_value == 0: HH_value = 24
    hh = str( HH_value - 12 if HH_value > 12 else HH_value )
    return "{hour}:{minute} {suffix}".format(
        hour=hh,
        minute=MM,
        suffix=("PM" if HH_value >= 12 and HH_value <= 23 else "AM")
    )

do_test(function_name="to_12", should_return="11:24 AM", time="1124")
do_test(function_name="to_12", should_return="9:00 AM", time="0900")
do_test(function_name="to_12", should_return="2:55 PM", time="1455")
do_test(function_name="to_12", should_return="11:46 PM", time="2346")
do_test(function_name="to_12", should_return="12:30 AM", time="0030")
