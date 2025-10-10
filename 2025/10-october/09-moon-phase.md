# Space Week Day 6: Moon Phase
*October 9, 2025*

For day six of Space Week, you will be given a date in the format `"YYYY-MM-DD"` and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

- `"New"`: days 1 - 7
- `"Waxing"`: days 8 - 14
- `"Full"`: days 15 - 21
- `"Waning"`: days 22 - 28

After day 28, the cycle repeats with day 1, a new moon.

- Use `"2000-01-06"` as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
- You will not be given any dates before the reference date.
- Return the correct phase as a string.

## Tests

1. `moon_phase("2000-01-12")` should return `"New"`.
2. `moon_phase("2000-01-13")` should return `"Waxing"`.
3. `moon_phase("2014-10-15")` should return `"Full"`.
4. `moon_phase("2012-10-21")` should return `"Waning"`.
5. `moon_phase("2022-12-14")` should return `"New"`.

## Solution

```python
from datetime import date

def moon_phase(date_string):
    # Get year, month, day from given string
    yyyy = int("".join(date_string[0:4]))
    mm = int("".join(date_string[5:7]))
    dd = int("".join(date_string[8:10]))

    # Init date value and reference date
    date_value = date(yyyy, mm, dd)
    reference_date = date(2000, 1, 6)

    # Calculate the difference between input date and reference date
    difference = date_value - reference_date

    # Determine the day is in which day of cycle
    num_of_date_in_cycle = 28
    days = (difference.days + 1) % num_of_date_in_cycle
    days = days if days != 0 else num_of_date_in_cycle

    # Return result
    if days <= 7: return "New"
    if days <= 14: return "Waxing"
    if days <= 21: return "Full"
    return "Waning"
```
