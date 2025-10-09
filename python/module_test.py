import inspect

# ANSI escape codes for colors
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def do_test(function_name: str, should_return, **kwargs) -> bool:
    """
    Executes a test for a specified function by name, using keyword arguments, and checks the result.

    Parameters:
        function_name (str): The name of the function to test. The function must be accessible in the caller's global scope.
        should_return (any): The expected return value from the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        bool: True if the function's return value matches `should_return`, False otherwise.

    Side Effects:
        Prints the function call, its result, and a colored PASS/FAIL message to the console.
    """
    # Preparation
    args = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
    test_function = inspect.currentframe().f_back.f_globals[function_name]

    # Test
    test_result = test_function(**kwargs)

    # Show test result
    print(f"{function_name}({args}) -> {test_result}")
    print("\t->",GREEN + "PASS" if test_result == should_return else RED + "FAIL", RESET)
    return test_result == should_return
