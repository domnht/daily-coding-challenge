# Phone Number Formatter

Given a string of ten digits, return the string as a phone number in this format: `"+D (DDD) DDD-DDDD"`.

## Tests

1. `format_number("05552340182")` should return `"+0 (555) 234-0182"`.
2. `format_number("15554354792")` should return `"+1 (555) 435-4792"`.

## Solution

```python
def format_number(number: str) -> str:
    if len(number) < 11 or not number.isnumeric(): return ""
    return "+{0} ({1}) {2}-{3}".format(
        number[0],
        "".join(number[1:4]),
        "".join(number[4:7]),
        "".join(number[7:11])
    )
```
