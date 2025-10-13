# Thermostat Adjuster

Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:

- Return `"heat"` if the current temperature is below the target.
- Return `"cool"` if the current temperature is above the target.
- Return `"hold"` if the current temperature is equal to the target.

## Tests

1. `adjust_thermostat(68, 72)` should return `"heat"`.
2. `adjust_thermostat(75, 72)` should return `"cool"`.
3. `adjust_thermostat(72, 72)` should return `"hold"`.
4. `adjust_thermostat(-20.5, -10.1)` should return `"heat"`.
5. `adjust_thermostat(100, 99.9)` should return `"cool"`.
6. `adjust_thermostat(0.0, 0.0)` should return `"hold"`.

## Solution

```python
def adjust_thermostat(temp, target):

    return temp
```
