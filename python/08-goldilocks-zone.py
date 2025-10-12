from module_test import *
from math import sqrt

def goldilocks_zone(mass: float) -> list:
    # Find the luminosity of the star
    luminosity = mass ** 3.5
    square_root = sqrt(luminosity)

    # Calculate the start and end distances
    start_distance = round(0.95 * square_root, 2)
    end_distance = round(1.37 * square_root, 2)

    return [start_distance, end_distance]

do_test(function_name="goldilocks_zone", should_return=[0.95, 1.37], mass=1)
do_test(function_name="goldilocks_zone", should_return=[0.28, 0.41], mass=0.5)
do_test(function_name="goldilocks_zone", should_return=[21.85, 31.51], mass=6)
do_test(function_name="goldilocks_zone", should_return=[9.38, 13.52], mass=3.7)
do_test(function_name="goldilocks_zone", should_return=[179.69, 259.13], mass=20)
