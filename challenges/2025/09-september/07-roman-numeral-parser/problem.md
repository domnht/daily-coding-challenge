# Roman Numeral Parser

Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

| Symbol | Value |
|:------:|:-----:|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

- Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added.

## Tests
1. `parse_roman_numeral("III")` should return `3`.
2. `parse_roman_numeral("IV")` should return `4`.
3. `parse_roman_numeral("XXVI")` should return `26`.
4. `parse_roman_numeral("XCIX")` should return `99`.
5. `parse_roman_numeral("CDLX")` should return `460`.
6. `parse_roman_numeral("DIV")` should return `504`.
7. `parse_roman_numeral("MMXXV")` should return `2025`.

## Solution

```python
def parse_roman_numeral(numeral):

    return numeral
```
