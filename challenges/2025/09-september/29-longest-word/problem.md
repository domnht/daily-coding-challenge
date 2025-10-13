# Longest Word

Given a sentence, return the longest word in the sentence.
- Ignore periods (`.`) when determining word length.
- If multiple words are ties for the longest, return the first one that occurs.

## Tests

1. `get_longest_word("coding is fun")` should return `"coding"`.
2. `get_longest_word("Coding challenges are fun and educational.")` should return `"educational"`.
3. `get_longest_word("This sentence has multiple long words.")` should return `"sentence"`.

## Solution

```python
def get_longest_word(sentence: str) -> str:
    words = sentence.replace(".", "").split(" ")
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word
```
