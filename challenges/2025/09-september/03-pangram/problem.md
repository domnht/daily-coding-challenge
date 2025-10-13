# Pangram

Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

- Ignore non-alphabetical characters in the word or sentence.
- Ignore letter casing in the word or sentence.

## Tests
1. `is_pangram("hello", "helo")` should return `True`.
2. `is_pangram("hello", "hel")` should return `False`.
3. `is_pangram("hello", "helow")` should return `False`.
4. `is_pangram("hello world", "helowrd")` should return `True`.
5. `is_pangram("Hello World!", "helowrd")` should return `True`.
6. `is_pangram("Hello World!", "heliowrd")` should return `False`.
7. `is_pangram("freeCodeCamp", "frcdmp")` should return `False`.
8. `is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz")` should return `True`.

## Solution

```python
def is_pangram(sentence, letters):

    return sentence
```