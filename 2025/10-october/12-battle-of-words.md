# Battle of Words
*October 12, 2025*

Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:
- The given sentences will always contain the same number of words.
- Words are separated by a single space and will only contain letters.
- The value of each word is the sum of its letters.
- Letters `a` to `z` correspond to the values `1` through `26`. For example, `a` is `1`, and `z` is `26`.
- A capital letter doubles the value of the letter. For example, `A` is `2`, and Z is `52`.
- Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
- A word wins if its value is greater than the opposing word's value.
- The team with more winning words is the winner.

Return `"We win"` if your team is the winner, `"We lose"` if your team loses, and `"Draw"` if both teams have the same number of wins.

## Tests
1. `battle("hello world", "hello word")` should return `"We win"`.
2. `battle("Hello world", "hello world")` should return `"We win"`.
3. `battle("lorem ipsum", "kitty ipsum")` should return `"We lose"`.
4. `battle("hello world", "world hello")` should return `"Draw"`.
5. `battle("git checkout", "git switch")` should return `"We win"`.
6. `battle("Cheeseburger with fries", "Cheeseburger with Fries")` should return `"We lose"`.
7. `battle("We must never surrender", "Our team must win")` should return `"Draw"`.

## Solution

```python
def battle(our_team: str, opponent: str) -> str:
    # Create list from two input sentences
    our_team_words = our_team.split(" ")
    opponent_words = opponent.split(" ")
    num_of_words = len(our_team_words)

    # Create value array for lower chars
    char_values = {}
    for i in range(ord("a"), ord("z") + 1):
        char_values[chr(i)] = i - ord("a") + 1

    num_of_our_winning_words = 0
    num_of_opponent_winning_words = 0
    for i in range(num_of_words):
        # Calculate word values (our team)
        our_value = 0
        for letter in our_team_words[i]:
            our_value += char_values[letter.lower()] * (1 if letter.islower() else 2)

        # Calculate word values (opponent team)
        opponent_value = 0
        for letter in opponent_words[i]:
            opponent_value += char_values[letter.lower()] * (1 if letter.islower() else 2)

        # Check if our word wins or loses
        if our_value > opponent_value:
            num_of_our_winning_words += 1
        if our_value < opponent_value:
            num_of_opponent_winning_words += 1

    # Return the battle result
    if num_of_our_winning_words > num_of_opponent_winning_words:
        return "We win"
    if num_of_our_winning_words < num_of_opponent_winning_words:
        return "We lose"
    return "Draw"
```
