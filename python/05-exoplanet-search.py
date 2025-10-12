from module_test import *

def has_exoplanet(readings: str) -> bool:
    luminosities = {}
    luminosity_v_alue = 0
    for code in list(range(ord("0"), ord("9")+1)) + list(range(ord("A"), ord("Z")+1)):
        luminosities[chr(code)] = luminosity_v_alue
        luminosity_v_alue += 1

    reading_luminosities = []
    total_luminosity = 0

    for char in readings:
        current_luminosity = luminosities[char]
        reading_luminosities.append(current_luminosity)
        total_luminosity += current_luminosity

    average_luminosity = total_luminosity / len(reading_luminosities)
    eighty_percent_of_average_luminosity = average_luminosity * 0.8
    for reading_luminosity in reading_luminosities:
        if reading_luminosity <= eighty_percent_of_average_luminosity:
            return True
    return False

do_test(function_name="has_exoplanet", should_return=False, readings="665544554")
do_test(function_name="has_exoplanet", should_return=True, readings="FGFFCFFGG")
do_test(function_name="has_exoplanet", should_return=False, readings="MONOPLONOMONPLNOMPNOMP")
do_test(function_name="has_exoplanet", should_return=True, readings="FREECODECAMP")
do_test(function_name="has_exoplanet", should_return=False, readings="9AB98AB9BC98A")
do_test(function_name="has_exoplanet", should_return=True, readings="ZXXWYZXYWYXZEGZXWYZXYGEE")
