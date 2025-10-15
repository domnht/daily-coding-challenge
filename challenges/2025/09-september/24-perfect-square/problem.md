# Perfect Square

Given an integer, determine if it is a perfect square.

- A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.

## Tests

1. `is_perfect_square(9)` should return `True`.
2. `is_perfect_square(49)` should return `True`.
3. `is_perfect_square(1)` should return `True`.
4. `is_perfect_square(2)` should return `False`.
5. `is_perfect_square(99)` should return `False`.
6. `is_perfect_square(-9)` should return `False`.
7. `is_perfect_square(0)` should return `True`.
8. `is_perfect_square(25281)` should return `True`.

## Solution

```python
from math import sqrt

def is_perfect_square(n):
    if n < 0: return False
    square_root_of_n = sqrt(n)
    return int(square_root_of_n) == square_root_of_n
```
