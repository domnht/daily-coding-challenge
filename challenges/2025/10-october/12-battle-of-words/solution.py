from module_test import do_test

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


do_test(function_name="battle", should_return="We win", our_team="hello world", opponent="hello word")
do_test(function_name="battle", should_return="We win", our_team="Hello world", opponent="hello world")
do_test(function_name="battle", should_return="We lose", our_team="lorem ipsum", opponent="kitty ipsum")
do_test(function_name="battle", should_return="Draw", our_team="hello world", opponent="world hello")
do_test(function_name="battle", should_return="We win", our_team="git checkout", opponent="git switch")
do_test(function_name="battle", should_return="We lose", our_team="Cheeseburger with fries", opponent="Cheeseburger with Fries")
do_test(function_name="battle", should_return="Draw", our_team="We must never surrender", opponent="Our team must win")
