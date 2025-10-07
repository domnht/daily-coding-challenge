# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def do_test(function_name: str, should_return, **kwargs) -> bool:
    # Preparation
    args = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
    test_function = globals()[function_name]

    # Test
    test_result = test_function(**kwargs)

    # Show test result
    print(f"{function_name}({args}) -> {test_result}")
    print("\t->",GREEN + "PASS" if test_result == should_return else RED + "FAIL", RESET)
    return test_result == should_return
