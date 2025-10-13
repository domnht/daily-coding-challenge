# 24 to 12
Given a string representing a time of the day in the 24-hour format of `"HHMM"`, return the time in its equivalent 12-hour format of `"H:MM AM"` or `"H:MM PM"`.

- The given input will always be a four-digit string in 24-hour time format, from `"0000"` to `"2359"`.

## Tests

1. `to_12("1124")` should return `"11:24 AM"`.
2. `to_12("0900")` should return `"9:00 AM"`.
3. `to_12("1455")` should return `"2:55 PM"`.
4. `to_12("2346")` should return `"11:46 PM"`.
5. `to_12("0030")` should return `"12:30 AM"`.

## Solution

```python
def to_12(time: str) -> str:
    HH = time[0] + time[1]
    MM = time[2] + time[3]
    HH_value = int(HH)
    if HH_value == 0: HH_value = 24
    hh = str( HH_value - 12 if HH_value > 12 else HH_value )
    return "{hour}:{minute} {suffix}".format(
        hour=hh,
        minute=MM,
        suffix=("PM" if HH_value >= 12 and HH_value <= 23 else "AM")
    )
```
