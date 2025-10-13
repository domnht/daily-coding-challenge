# Space Week Day 3: Phone Home
*October 6, 2025*

For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

- The first value in the array is the distance from your location to the first satellite.
- Each subsequent value, except for the last, is the distance to the next satellite.
- The last value in the array is the distance from the previous satellite to your home planet.
- The message travels at 300,000 km/s.
- Each satellite the message passes through adds a 0.5 second transmission delay.
- Return a number rounded to 4 decimal places, with trailing zeros removed.

## Tests

1. `send_message([300000, 300000])` should return `2.5`.
2. `send_message([384400, 384400])` should return `3.0627`.
3. `send_message([54600000, 54600000])` should return `364.5`.
4. `send_message([1000000, 500000000, 1000000])` should return `1674.3333`.
5. `send_message([10000, 21339, 50000, 31243, 10000])` should return `2.4086`.
6. `send_message([802101, 725994, 112808, 3625770, 481239])` should return `21.1597`.

## Solution

```python
def send_message(route: list) -> float:
    num_of_salleties = len(route) - 1
    total_distance = 0
    for i in range(0, len(route)):
        total_distance += route[i]

    return round(total_distance/300000 + 0.5*num_of_salleties, 4)
```
