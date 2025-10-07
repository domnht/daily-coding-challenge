# Space Week Day 2: Exoplanet Search
*October 5, 2025*

For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

- Luminosity readings only comprise of characters `0-9` and `A-Z` where each reading corresponds to the following numerical values:
- Characters `0-9` correspond to luminosity levels `0-9`.
- Characters `A-Z` correspond to luminosity levels `10-35`.

A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.

## Tests

1. `has_exoplanet("665544554")` should return `False`.
2. `has_exoplanet("FGFFCFFGG")` should return `True`.
3. `has_exoplanet("MONOPLONOMONPLNOMPNOMP")` should return `False`.
4. `has_exoplanet("FREECODECAMP")` should return `True`.
5. `has_exoplanet("9AB98AB9BC98A")` should return `False`.
6. `has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE")` should return `True`.

## Solution

```python
def has_exoplanet(readings):
    luminosities = {}
    luminosity_v_alue = 0
    for code in list(range(ord("0"), ord("9")+1)) + list(range(ord("A"), ord("Z")+1)):
        luminosities[chr(code)] = luminosity_v_alue
        luminosity_v_alue += 1

    reading_luminosities = []
    total_luminosity = 0

    for char in readings:
        current_luminosity = luminosities[char]
        reading_luminosities.append(current_luminosity)
        total_luminosity += current_luminosity

    average_luminosity = total_luminosity / len(reading_luminosities)
    eighty_percent_of_average_luminosity = average_luminosity * 0.8
    for reading_luminosity in reading_luminosities:
        if reading_luminosity <= eighty_percent_of_average_luminosity:
            return True
    return False
```
