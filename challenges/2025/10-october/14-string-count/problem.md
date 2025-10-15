# String Count

Given two strings, determine how many times the second string appears in the first.

- The pattern string can overlap in the first string. For example, `"aaa"` contains `"aa"` twice. The first two `a`'s and the second two.

## Tests

1. `count('abcdefg', 'def')` should return `1`.
2. `count('hello', 'world')` should return `0`.
3. `count('mississippi', 'iss')` should return `2`.
4. `count('she sells seashells by the seashore', 'sh')` should return `3`.
5. `count('101010101010101010101', '101')` should return `10`.

## Solution

```python
def count(text: str, parameter: str) -> int:
    num_of_found = 0
    current_found_position = -1
    for i in range(len(text) - len(parameter) + 1):
        find_result = text.find(parameter, i)
        if find_result >= 0 and find_result != current_found_position:
            num_of_found += 1
            current_found_position = find_result

    return num_of_found
```
