# Space Week Day 7: Launch Fuel
*October 10, 2025*

For the final day of Space Week, you will be given the mass in kilograms (kg) of a payload you want to send to orbit. Determine the amount of fuel needed to send your payload to orbit using the following rules:

- Rockets require 1 kg of fuel per 5 kg of mass they must lift.
- Fuel itself has mass. So when you add fuel, the mass to lift goes up, which requires more fuel, which increases the mass, and so on.
- To calculate the total fuel needed: start with the payload mass, calculate the fuel needed for that, add that fuel to the total mass, and calculate again. Repeat this process until the additional fuel required is less than 1 kg, then stop.
- Ignore the mass of the rocket itself. Only compute fuel needed to lift the payload and its own fuel.

For example, given a payload mass of 50 kg, you would need 10 kg of fuel to lift it (payload / 5), which increases the total mass to 60 kg, which needs 12 kg to lift (2 additional kg), which increases the total mass to 62 kg, which needs 12.4 kg to lift - 0.4 additional kg - which is less 1 additional kg, so we stop here. The total mass to lift is 62.4 kg, 50 of which is the initial payload and 12.4 of fuel.

- Return the amount of fuel needed rounded to one decimal place.

## Tests
1. `launch_fuel(50)` should return `12.4`.
2. `launch_fuel(500)` should return `124.8`.
3. `launch_fuel(243)` should return `60.7`.
4. `launch_fuel(11000)` should return `2749.8`.
5. `launch_fuel(6214)` should return `1553.4`.

## Solution

```python
def launch_fuel(payload: int) -> float:
    total_fuel = 0
    current_added_fuel = -1 # Use -1 as initial value

    while current_added_fuel >= 1 or current_added_fuel == -1:
        # Calculate the added fuel after adding fuel mass into total payload mass
        current_added_fuel = (payload + total_fuel) / 5 - total_fuel
        total_fuel += current_added_fuel

    return round(total_fuel, 1)
```