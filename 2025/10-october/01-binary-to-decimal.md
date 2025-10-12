# Binary to Decimal
*October 1, 2025*

Given a string representing a binary number, return its decimal equivalent as a number.

A binary number uses only the digits `0` and `1` to represent any number. To convert binary to decimal, multiply each digit by a power of `2` and add them together. Start by multiplying the rightmost digit by `2^0`, the next digit to the left by `2^1`, and so on. Once all digits have been multiplied by a power of `2`, add the result together.

For example, the binary number `101` equals `5` in decimal because:

```
1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
```

## Tests

1. `to_decimal("101")` should return `5`.
2. `to_decimal("1010")` should return `10`.
3. `to_decimal("10010")` should return `18`.
4. `to_decimal("1010101")` should return `85`.

## Solution

```python
def to_decimal(binary: str) -> int:
    decimal_result = 0
    num_of_chars = len(binary)
    for char in binary:
        num_of_chars -= 1
        decimal_result += int(char) * 2 ** num_of_chars
    return decimal_result
```
