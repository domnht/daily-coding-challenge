from module_test import *

def classification(temp):
    if temp >= 30000: return "O"
    if temp >= 10000: return "B"
    if temp >= 7500: return "A"
    if temp >= 6000: return "F"
    if temp >= 5200: return "G"
    if temp >= 3700: return "K"
    return "M"

do_test(function_name="classification", should_return="G", temp=5778)
do_test(function_name="classification", should_return="M", temp=2400)
do_test(function_name="classification", should_return="A", temp=9999)
do_test(function_name="classification", should_return="K", temp=3700)
do_test(function_name="classification", should_return="M", temp=3699)
do_test(function_name="classification", should_return="O", temp=210000)
do_test(function_name="classification", should_return="F", temp=6000)
do_test(function_name="classification", should_return="B", temp=11432)
