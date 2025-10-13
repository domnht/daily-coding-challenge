# 2nd Largest
*September 25, 2025*

Given an array, return the second largest distinct number.

## Tests

1. `second_largest([1, 2, 3, 4])` should return `3`.
2. `second_largest([20, 139, 94, 67, 31])` should return `94`.
3. `second_largest([2, 3, 4, 6, 6])` should return `4`.
4. `second_largest([10, -17, 55.5, 44, 91, 0])` should return `55.5`.
5. `second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0])` should return `0`.

## Solution

```python
def second_largest(arr):
    larges_1 = arr[0]
    larges_2 = arr[1]
    for number in arr:
        if number < larges_1 and larges_2 == larges_1:
            larges_2 = number
        if number > larges_2:
            if number > larges_1:
                larges_2 = larges_1
                larges_1 = number
            if number < larges_1:
                larges_2 = number
    return larges_2
```
