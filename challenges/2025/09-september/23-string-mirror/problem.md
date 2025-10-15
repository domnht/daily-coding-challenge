# String Mirror

Given two strings, determine if the second string is a mirror of the first.

- A string is considered a mirror if it contains the same letters in reverse order.
- Treat uppercase and lowercase letters as distinct.
- Ignore all non-alphabetical characters.

## Tests

1. `is_mirror("helloworld", "helloworld")` should return `False`.
2. `is_mirror("Hello World", "dlroW olleH")` should return `True`.
3. `is_mirror("RaceCar", "raCecaR")` should return `True`.
4. `is_mirror("RaceCar", "RaceCar")` should return `False`.
5. `is_mirror("Mirror", "rorrim")` should return `False`.
6. `is_mirror("Hello World", "dlroW-olleH")` should return `True`.
7. `is_mirror("Hello World", "!dlroW !olleH")` should return `True`.

## Solution

```python
def is_mirror(str1: str, str2: str) -> bool:
    str1_without_symbol = "".join(char for char in str1 if char.isalpha())
    str2_without_symbol = "".join(char for char in str2 if char.isalpha())
    return str1_without_symbol == str2_without_symbol[::-1]
```
