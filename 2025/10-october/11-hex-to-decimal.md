# Hex to Decimal
*October 11, 2025*

Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

- `0-9` represent values `0` through `9`.
- `A-F` represent values `10` through `15`.

Here's a partial conversion table:

| Hexadecimal | Decimal |
|:-----------:|:-------:|
| 0           | 0       |
| 1           | 1       |
| ...         | ...     |
| 9           | 9       |
| A           | 10      |
| ...         | ...     |
| F           | 15      |
| 10          | 16      |
| ...         | ...     |
| 9F          | 159     |
| A0          | 160     |
| ...         | ...     |
| FF          | 255     |
| 100         | 256     |
|-------------|---------|

- The string will only contain characters 0–9 and A–F.

## Tests
1. `hex_to_decimal("A")` should return `10`.
2. `hex_to_decimal("15")` should return `21`.
3. `hex_to_decimal("2E")` should return `46`.
4. `hex_to_decimal("FF")` should return `255`.
5. `hex_to_decimal("A3F")` should return `2623`.

## Solution

```python
def hex_to_decimal(hex: str):
    hex_chars = list(range(0, 10)) + list(["A", "B", "C", "D", "E", "F"])
    decimal_values = {}
    for i in range(0, 16):
        decimal_values[str(hex_chars[i])] = i

    decimal_result = 0
    num_of_chars = len(hex)
    for char in hex:
        num_of_chars -= 1
        decimal_result += decimal_values[char] * 16 ** num_of_chars
    return decimal_result
```
