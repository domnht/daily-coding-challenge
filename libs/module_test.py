import time
import inspect

# Output terminal color constants
# Format
BOLD = "\033[1m"
ITALIC = "\u001b[3m"

# Foreground
FG_BLACK = "\033[30m"
FG_RED = "\033[31m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"
FG_BLUE = "\033[34m"
FG_MAGENTA = "\033[35m"
FG_CYAN = "\033[36m"
FG_WHITE = "\033[37m"
FG_MAGENTA = "\x1b[35m"
FG_BRIGHT_BLACK = "\033[90m"  # Also known as Dark Gray
FG_BRIGHT_RED = "\033[91m"
FG_BRIGHT_GREEN = "\033[92m"
FG_BRIGHT_YELLOW = "\033[93m"
FG_BRIGHT_BLUE = "\033[94m"
FG_BRIGHT_MAGENTA = "\033[95m"
FG_BRIGHT_CYAN = "\033[96m"
FG_BRIGHT_WHITE = "\033[97m"

# Background
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
BG_BRIGHT_BLACK = "\033[100m"
BG_BRIGHT_RED = "\033[101m"
BG_BRIGHT_GREEN = "\033[102m"
BG_BRIGHT_YELLOW = "\033[103m"
BG_BRIGHT_BLUE = "\033[104m"
BG_BRIGHT_MAGENTA = "\033[105m"
BG_BRIGHT_CYAN = "\033[106m"
BG_BRIGHT_WHITE = "\033[107m"

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

    print(f"{BG_BRIGHT_CYAN+FG_BLACK}TESTING{RESET} {BOLD}{function_name}{RESET}{FG_BRIGHT_BLACK}({args}){RESET}")

    # Test
    start_time = time.time()
    test_result = test_function(**kwargs)
    end_time = time.time()

    # Show test result
    print(f"    -> {test_result} {FG_BRIGHT_BLACK}({round((end_time - start_time) * 1000, 10)} ms){RESET}")
    print(f"    -> {FG_GREEN + "PASS" if test_result == should_return else FG_RED + "FAIL"}{RESET}")
    return test_result == should_return

