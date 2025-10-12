# Space Week Day 5: Goldilocks Zone
*October 8, 2025*

For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

1. Find the luminosity of the star by raising its mass to the power of 3.5.
2. The start of the zone is 0.95 times the square root of its luminosity.
3. The end of the zone is 1.37 times the square root of its luminosity.
- Return the distances rounded to two decimal places.

For example, given `1` as a mass, return `[0.95, 1.37]`.

## Tests

1. `goldilocks_zone(1)` should return `[0.95, 1.37]`.
2. `goldilocks_zone(0.5)` should return `[0.28, 0.41]`.
3. `goldilocks_zone(6)` should return `[21.85, 31.51]`.
4. `goldilocks_zone(3.7)` should return `[9.38, 13.52]`.
5. `goldilocks_zone(20)` should return `[179.69, 259.13]`.

## Solution

```python
from math import sqrt

def goldilocks_zone(mass: float) -> list:
    # Find the luminosity of the star
    luminosity = mass ** 3.5
    square_root = sqrt(luminosity)

    # Calculate the start and end distances
    start_distance = round(0.95 * square_root, 2)
    end_distance = round(1.37 * square_root, 2)

    return [start_distance, end_distance]
```
