# Space Week Day 4: Landing Spot
*October 7, 2025*

In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

- Each spot in the matrix will contain a number from 0-9, inclusive.
- Any 0 represents a potential landing spot.
- Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
- The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
- Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
- Return the indices of the safest landing spot. There will always only be one safest spot.

For instance, given:

```python
[
    [1, 0],
    [2, 0]
]
```

Return `[0, 1]`, the indices for the `0` in the first array.

## Tests

1. `find_landing_spot([[1, 0], [2, 0]])` should return `[0, 1]`.
2. `find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]])` should return `[1, 1]`.
3. `find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]])` should return `[2, 2]`.
4. `find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]])` should return `[2, 1]`.

## Solution

```python
def find_landing_spot(matrix) -> list:
    min = -1
    target_i = -1
    target_j = -1

    height = len(matrix)
    width = len(matrix[0])

    for i in range(0, height):
        for j in range(0, width):
            # Check if current position is 0
            if matrix[i][j] > 0: continue

            # Caculate sum of (up to) 4 neighbors
            sum = matrix[i][j]
            if i - 1 >= 0:     sum += matrix[i - 1][j]
            if i + 1 < height: sum += matrix[i + 1][j]
            if j - 1 >= 0:     sum += matrix[i][j - 1]
            if j + 1 < width:  sum += matrix[i][j + 1]

            # Compare and assign new min value
            if min == -1 or min > sum:
                target_i = i
                target_j = j
                min = sum

    return [target_i, target_j]
```
